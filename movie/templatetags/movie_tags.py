from django import template


register = template.Library()

@register.filter
def index(List, i):
    return List[int(i)].title.upper()

@register.filter
def index1(List, i):
    return List[int(i)].director


@register.filter
def index2(List, i):
    return List[int(i)].review_mov


@register.filter
def index3(List, i):
    return List[int(i)].imdb_rating


@register.filter
def index4(List, i):
    return List[int(i)].year


@register.filter
def index5(List, i):
    return List[int(i)].genre

@register.filter
def index6(List, i):
    return List[int(i)].id

@register.filter
def index7(List, i):
    return List[int(i)].img

@register.filter
def cap(String):
    return String.upper()

@register.filter
def rating(Dict, i):
    return Dict[i]

@register.filter
def new(List):
    return List[0].upper()
