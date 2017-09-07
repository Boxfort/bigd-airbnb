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

#TODO: Check if filename of city exists, if not then call the plotter to make the file.
def city(request, city_name):
    template = loader.get_template('map/map.html')
    filepath = plotter.plot_heatmap(city_name, "price")
    error = None
    map_file = ""
    if filepath == None:
        city_name = "Something went wrong!"
        error = urllib.urlopen(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'blankmap.html')).read()
    else:
        map_file = urllib.urlopen(filepath).read()

    context = {
        'city_name': city_name,
        'map_file': map_file,
        'error': error
    }
    return HttpResponse(template.render(context, request))
