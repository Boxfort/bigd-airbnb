from django.conf.urls import url
from . import views

urlpatterns = [
    #/map/
    url(r'^$', views.index, name='index'),
    url(r'^city_post/$', views.city_post, name='city_post'),
    #/map/heatmap/CITY_NAME/WEIGHT_ON
    url(r'^heatmap/(?P<city_name>.+)/(?P<weight_on>.+)/$', views.city_heatmap, name='city_heatmap'),
    #/map/pins/CITY_NAME/
    url(r'^pins/(?P<city_name>.+)/$', views.city_pins, name='city_pins'),
]
