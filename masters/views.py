from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
from django.template import RequestContext


def index(request):
    context = RequestContext(request)
    
    context_dict = {'bodymessage': "I'm bold font from context"}
    
    return render_to_response('masters/index.html', context_dict ,context) 

def about(request):
    return HttpResponse("Master about page! <a href='/masters'>Index</a>")