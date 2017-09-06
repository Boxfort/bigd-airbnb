import pandas as pd 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'gmplot'))
import gmplot

#TODO: Pull city information from firebase
#def plot_heatmap(city_name, weight_on):
if __name__ == '__main__':
    filename = 'tomslee_airbnb_aarhus_1481_2017-07-28.csv'
    filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', filename)

    data = pd.read_csv(filepath, sep=',')
    lats = data['latitude']
    longs = data['longitude']
    weights = data['price']

    #gmap = gmplot.GoogleMapPlotter(lats[0], longs[0], 16)
    gmap = gmplot.GoogleMapPlotter.from_geocode("aarhus")
    gmap.heatmap_weight(lats, longs, weights)

    gmap.draw('test.html')
