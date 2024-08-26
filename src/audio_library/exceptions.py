from django.http import Http404
from django.shortcuts import get_object_or_404

def custom_get_object_or_404(model_class, **kwargs):
    try:
        return model_class.objects.get(**kwargs)
    except model_class.DoesNotExist:
        raise Http404("This track is private, please provide credentials")