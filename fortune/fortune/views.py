from django.shortcuts import render

from django.http import HttpResponse

def get_fortune(request):
    return HttpResponse("Here is a fortune")