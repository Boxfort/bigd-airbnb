# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import urllib.request
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'scripts'))
import plotter

# Create your views here.

def index(request):
    template = loader.get_template('map/index.html')
    context = {
            'thing_1' : 'This is thing one',
            'thing_2' : 'This is thing two',
            }
    return HttpResponse(template.render(context, request))

def city(request, city_name):
    template = loader.get_template('map/map.html')
    map_file = urllib.request.urlopen('file://' + os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.html")).read()
    print("hehehehe")
    context = {
        'city_name': city_name,
        'map_file': map_file,
        'thing_3' : 'okay',
    }
    return HttpResponse(template.render(context, request))
