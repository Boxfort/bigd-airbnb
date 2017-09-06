# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import urllib
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'scripts'))
import plotter

# Create your views here.

def index(request):
    return HttpResponse("<h1>Map index page</h1>")

def city(request, city_name):
    template = loader.get_template('map/map.html')
    map_file = urllib.urlopen(os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.html")).read()
    
    context = {
        'city_name': city_name,
        'map_file': map_file,
    }
    return HttpResponse(template.render(context, request))
