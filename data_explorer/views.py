from django.http import HttpResponse
from django.apps import apps

from lys import L


def index(requests):
    app = apps.get_app_config('core')

    html_names = []
    for model_name, model in app.models.items():
        html_names.append(L.li / L.a(href='/'+model_name + '/') / model_name)

    return HttpResponse(str(L.ul / html_names))


def model(requests, model_name):
    app = apps.get_app_config('core')
    model = app.models[model_name]
    return HttpResponse(str(L.ul / (
        (
            L.li / L.a(href='/'+model_name+'/'+obj.pk) / str(obj)
        ) for obj in model.objects.all()
    )))


def obj(requests, model_name, pk):
    app = apps.get_app_config('core')
    model = app.models[model_name]
    obj = model.objects.get(pk=pk)
    return HttpResponse(str(L.ul / (
        (
            L.li / f"{field.name}: {getattr(obj, field.name)}"
        ) for field in model._meta.get_fields() if field.related_model is None
    )))