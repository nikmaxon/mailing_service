from django import template

register = template.Library()

# Создание фильтра
@register.filter()
def mediapath(text):
    if text:
        return f"/media/{text}"
    else:
        return '#'