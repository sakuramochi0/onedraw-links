from django import template

register = template.Library()

@register.filter
def addclass(val, arg):
    return val.as_widget(attrs={'class': arg})

@register.filter
def label(val, arg):
    return val.label_tag(arg)
