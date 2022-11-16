from django.core.paginator import Paginator


def paginate(objects_list, request, per_page):
    paginator = Paginator(objects_list, per_page)
    return paginator


def paginator_range(page_number, pages_count, paginator_border):
    if page_number - paginator_border <= 0:
        left = 1
    else:
        left = page_number - paginator_border
    if page_number + paginator_border > pages_count:
        right = pages_count
    else:
        right = page_number + paginator_border
    return range(left, right)


def validate_parameters(parameter, item_range):
    if not (isinstance(parameter, int)):
        return 1
    if parameter < 0 or parameter > item_range:
        return 1
    else:
        return parameter
