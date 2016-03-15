from django.shortcuts import render

def test(request, *args, **kwargs):
    return HttpResponse('OK')

# Create your views here.
