from django.shortcuts import render
from django.template import loader
from django.http.response import HttpResponse
from django.template import Context

def reg(request):
    view = "reg"
    template = loader.get_template('templates/reg.html')
    html = template.render(Context({'name':view}))
    return HttpResponse(html)

