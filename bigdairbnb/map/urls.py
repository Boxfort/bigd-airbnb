from django.conf.urls import url
from . import views

urlpatterns = [
    #/map/
    url(r'^$', views.index, name='index'),
    #/map/CITY_NAME/
    url(r'^(?P<city_name>[A-z]+)/$', views.city, name='city')
]
