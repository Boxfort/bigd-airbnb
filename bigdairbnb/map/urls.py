from django.conf.urls import url
from . import views

urlpatterns = [
    #/map/
    url(r'^$', views.index, name='index'),
    url(r'^city_post/$', views.city_post, name='city_post'),
    #/map/heatmap/CITY_NAME/WEIGHT_ON
    url(r'^heatmap/(?P<city_name>[A-z]+)/(?P<weight_on>[A-z]+)/$', views.city_heatmap, name='city_heatmap'),
    #/map/pins/CITY_NAME/
    url(r'^pins/(?P<city_name>[A-z]+)/$', views.city_pins, name='city_pins'),
]
