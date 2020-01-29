from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def  home_page_view(request):
    return HttpResponse('hi world please listen to meeeeeee| \n now you able to hear me or not')
