import pandas as pd 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'gmplot'))
import gmplot
import pyrebase

config = {
    "apiKey": "API KEY",
    "authDomain": "PROJECT.firebaseapp.com",
    "databaseURL": "https://PROJECT.firebaseio.com",
    "storageBucket": "PROJECT.appspot.com",
    "serviceAccount": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'firebase', 'KEY.json')
}

#TODO: Pull city information from firebase
#      re-structure database
def plot_heatmap(city_name, weight_on):
#if __name__ == '__main__':

    filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "heatmaps", city_name + ".html")

    #If a heatmap has already been generated return the filepath to it.
    if(os.path.exists(filepath)):
       print "file exists"
       return filepath

    try:
        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()
        #authenticate a user
        user = auth.sign_in_with_email_and_password("EMAIL", "PASSWORD")
        db = firebase.database()
        data = db.child('listing').order_by_child("city").equal_to(city_name).get(user['idToken'])

        data = list(data.val().items())

        lats = []
        longs = []
        weights = []
        
        for entry in data:
            lats.append(float(entry[1]['latitude']))
            longs.append(float(entry[1]['longitude']))
            weights.append(float(entry[1]['price']))

        #lats = data['latitude']
        #longs = data['longitude']
        #weights = data[weight_on]

        gmap = gmplot.GoogleMapPlotter(lats[0], longs[0], 16)
        gmap = gmplot.GoogleMapPlotter.from_geocode(city_name)
        gmap.heatmap_weight(lats, longs, weights)

        gmap.draw(os.path.join(os.path.dirname(os.path.realpath(__file__)), "heatmaps", city_name + ".html"))
    except Exception, e:
        print str(e)
        return None

    return filepath
