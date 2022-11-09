from django.core.paginator import Paginator


def paginate(objects_list, request, per_page):
    p = Paginator(objects_list, 3)
    page = p.page(per_page)
    return page