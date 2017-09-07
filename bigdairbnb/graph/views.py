# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'scripts'))
import grapher

# Create your views here.

def index(request):
    template = loader.get_template('graph/graph.html')
    context = {
        "graph_html" : None
        }
    return HttpResponse(template.render(context, request))

def graph(request, city1, city2, field):
    template = loader.get_template('graph/graph.html')
    graph_html = grapher.graph(city1, city2, field)
    context = {
        "graph_html" : graph_html
        }
    return HttpResponse(template.render(context, request))

def graph_post(request):
    city1 = request.POST.get("city1")
    city2 = request.POST.get("city2")
    field = request.POST.get("field")
    return graph(request, city1, city2, field)
