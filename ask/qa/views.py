from django.shortcuts import render

#try
from django.http import HttpResponse

def test(request, *args, **kwargs):
    return HttpResponse('OK')

# Create your views here.
