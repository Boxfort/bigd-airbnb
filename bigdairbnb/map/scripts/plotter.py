import pandas as pd 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'gmplot'))
import gmplot

filename = 'tomslee_airbnb_aarhus_1481_2017-07-28.csv'
filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', filename)

data = pd.read_csv(filepath, sep=',')
lats = data['latitude']
longs = data['longitude']
weights = data['price']

gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 16)
gmap.heatmap_weight(lats, longs, weights)

gmap.draw('test.html')
