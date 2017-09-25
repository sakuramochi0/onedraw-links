from django.shortcuts import render
from django.forms import modelform_factory

from .models import Onedraw


def index(request):
    return render(request, 'onedraw_links/index.html', {'onedraws': Onedraw.objects.all})


def new(request):
    OnedrawFormset = modelform_factory(Onedraw, fields='__all__')
    formset = OnedrawFormset()
    return render(request, 'onedraw_links/new.html', {'formset': formset})

def new_confirm(request):
    try:
        onedraw = Onedraw.objects.get(pk=request.POST.get('screen_name'))
        return render(request, 'onedraw_links/new-confirm.html',
                      {'waring_message': 'このアカウント (@{}) は既に登録されています。'.format(
                          onedraw.screen_name)})
    except Onedraw.DoesNotExist:
        onedraw = Onedraw.objects.create(
            name=request.POST.get('name'),
            screen_name=request.POST.get('screen_name'),
            work=request.POST.get('work'),
            genre=request.POST.get('genre'),
            rule_url=request.POST.get('rule_url'),
            rt_screen_name=request.POST.get('rt_screen_name'),
            collection_url=request.POST.get('collection_url'),
            langs=request.POST.get('langs').split(','),
        )
        return render(request, 'onedraw_links/new-confirm.html', {'onedraw': onedraw})
