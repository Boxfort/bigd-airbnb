# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse
import urllib
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'scripts'))
import plotter

# Create your views here.

def index(request):
    template = loader.get_template('map/map.html')
    error = urllib.urlopen(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'blankmap.html')).read()
    city_name = "Select a city!"
    context = {
        'city_name': city_name,
        'error':error
    }
    return HttpResponse(template.render(context, request))

#TODO: Check if filename of city exists, if not then call the plotter to make the file.
def city_heatmap(request, city_name, weight_on):
    template = loader.get_template('map/map.html')
    filepath = plotter.plot_heatmap(city_name, weight_on)
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
        'weight_on': weight_on,
        'error': error
    }
    return HttpResponse(template.render(context, request))

def city_pins(request, city_name):
    template = loader.get_template('map/map.html')
    filepath = plotter.plot_pins(city_name)
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

def city_post(request):
    #HANDLE MAP TYPES AND REDIRECT AS APROPRIATE
    city = request.POST.get("city")
    weight = request.POST.get("weight")
    maptype = request.POST.get("type")
    print "posting with values " + city + " and  " + weight 
    if maptype == "heatmap":
        return redirect('/map/'+ maptype + "/" + city + '/' + weight)
    elif maptype == "pins":
        return redirect('/map/'+ maptype + "/" + city + '/')
    else:
        return HttpResonse("Something has went horribly wrong, you should never see this error.")
