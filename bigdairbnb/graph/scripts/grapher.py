import os
import sys
import pyrebase
import plotly
import plotly.plotly as py
import plotly.offline as pyo
import plotly.graph_objs as go

config = {
    "apiKey": "AIzaSyAuwjUrnZmJg3-iiREyfgcVCM3O47FKuLc",
    "authDomain": "airbnb-36a85.firebaseapp.com",
    "databaseURL": "https://airbnb-36a85.firebaseio.com",
    "storageBucket": "airbnb-36a85.appspot.com",
    "serviceAccount": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'firebase', 'airbnb-36a85-firebase-adminsdk-2v4vn-c034499121.json')
}


def graph(city1, city2, field):
    filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "graphs", city1 + "_" + city2 + "_" + field + ".html")

    #If a heatmap has already been generated return the filepath to it.
    if(os.path.exists(filepath)):
       print "file exists"
       return filepath

    try:
        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()
        #authenticate a user
        user = auth.sign_in_with_email_and_password("jackandherson@gmail.com", "firebasepassword")
        db = firebase.database()
        data = db.child('listing').order_by_child("city").equal_to(str(city1)).get(user['idToken'])
        data2 = db.child('listing').order_by_child("city").equal_to(str(city2)).get(user['idToken'])
        city1list = list(data.val().items())
        city2list = list(data2.val().items())
        

        series1 = []
        series2 = []

        for entry in city1list:
            series1.append(float(entry[1][str(field)]))

        for entry in city2list:
            series2.append(float(entry[1][str(field)]))

        value1 = sum(series1) / float(len(series1))
        value2 = sum(series2) / float(len(series2))

        bar_data = [go.Bar(
                x=[city1, city2],
                y=[value1,value2]
            )]

        htmlfile = open(filepath, "w")
        htmlfile.write(pyo.plot(bar_data, include_plotlyjs=False, output_type='div'))
        htmlfile.close()

    except Exception, e:
        print str(e)
        return None

    return filepath
