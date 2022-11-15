from django.shortcuts import render
from . import models, utils


def index(request):
    page = request.GET.get("page", 1)
    items_list = list(models.Ask.objects.get_all_asks_by_date())
    paginator = utils.paginate(items_list, request, 3)
    page = utils.validate_parameters(page, paginator.num_pages)
    context = {"questions": paginator.page(page),
               "pages_count": utils.paginator_range(int(page), paginator.num_pages, 6)}
    return render(request, 'index.html', context=context)


def hot(request):
    page = request.GET.get("page", 1)
    items_list = list(models.Ask.objects.get_best_ask())
    paginator = utils.paginate(items_list, request, 3)
    page = utils.validate_parameters(page, paginator.num_pages)
    context = {"questions": paginator.page(page),
               "pages_count": utils.paginator_range(int(page), paginator.num_pages, 6), "added_title": "Best"}
    return render(request, 'index.html', context=context)


def question(request, question_id: int):
    page = request.GET.get("page", 1)
    question_item = models.Ask.objects.get(id=question_id)
    paginator = utils.paginate(question_item.answers.all(), request, 2)
    page = utils.validate_parameters(page, paginator.num_pages)
    context = {"question": question_item, "answers": paginator.page(page),
               "pages_count": utils.paginator_range(int(page), paginator.num_pages, 6)}
    return render(request, 'question.html', context=context)


def tag(request):
    tag_name = request.GET.get("tag_req", '')
    p = models.Ask.objects.get_ask_by_tag(tag_name)
    context = {"questions": p, "added_title": tag_name}
    return render(request, 'index.html', context=context)


def login(request):
    return render(request, 'login.html')


def ask(request):
    return render(request, 'ask.html')


def settings(request):
    return render(request, 'settings.html')


def signup(request):
    return render(request, 'signup.html')


def handler404(request, exception, template_name="404.html"):
    response = render(request, '404.html', status=404)
    response.status_code = 404
    return response

