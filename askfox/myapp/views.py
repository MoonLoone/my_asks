from heapq import nlargest
from .utils import paginate
from django.shortcuts import render
from . import models


def index(request):
    page = request.GET.get("page", 1)
    p = paginate(models.QUESTIONS, request, page)
    r = range(1, len(models.QUESTIONS) // 2)
    context = {"questions": p.object_list, "pages_count": r}
    return render(request, 'index.html', context=context)


def hot(request):
    page = request.GET.get("page", 1)
    l = []
    best_questions = []
    for i in range(len(models.QUESTIONS)):
        l.append(models.QUESTIONS[i]['answers_number'])
    res = nlargest(6, l)
    for i in range(len(models.QUESTIONS)):
        if res.__contains__(models.QUESTIONS[i]['answers_number']):
            best_questions.append(models.QUESTIONS[i])
    best_questions.reverse()
    r = range(1, len(best_questions) // 2)
    p = paginate(best_questions, request, page)
    context = {"questions": p, "pages_count": r}
    return render(request, 'index.html', context=context)


def question(request, question_id: int):
    question_item = models.QUESTIONS[question_id]
    page = request.GET.get("page", 1)
    answers = models.ANSWERS[question_id]
    r = range(1, question_item['answers_number'] // 2)
    if len(r) > 10:
        r = range(len(r) - 10, len(r))
    p = paginate(answers, request, page)
    context = {"question": question_item, "pages_count": r, "answers": p.object_list}
    return render(request, 'question.html', context=context)


def login(request):
    return render(request, 'login.html')


def ask(request):
    return render(request, 'ask.html')


def settings(request):
    return render(request, 'settings.html')


def signup(request):
    return render(request, 'signup.html')


def tag(request, tag_name: str):
    question_with_tag = []
    page = request.GET.get("page", 1)
    for i in range(len(models.QUESTIONS)):
        if models.QUESTIONS[i]['tags'].__contains__(tag_name):
            question_with_tag.append(models.QUESTIONS[i])
    p = paginate(question_with_tag, request, page)
    r = range(1, len(question_with_tag) // 2)
    context = {"questions": p.object_list, "pages_count": r, "tag_title": tag_name}
    return render(request, 'index.html', context=context)


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
