from django.conf.urls import url
from . import views

urlpatterns = [
    #/map/
    url(r'^$', views.index, name='index'),
    url(r'^city_post/$', views.city_post, name='city_post'),
    #/map/CITY_NAME/
    url(r'^(?P<city_name>[A-z]+)/$', views.city, name='city'),
    #/map/CITY_NAME/WEIGHT_ON
    url(r'^(?P<city_name>[A-z]+)/(?P<weight_on>[A-z]+)/$', views.city_weight, name='city_weight'),
]
