from django.conf.urls import url
from . import views

urlpatterns = [
    #/graph/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<city1>.+)/(?P<city2>.+)/(?P<field>[A-z]+)/$', views.graph, name='graph'),
    url(r'^graph_post/$', views.graph_post, name="graph_post")
    #url(r'^test/$', views.city_post, name='city_post'),
    #url(r'^pins/(?P<city_name>[A-z]+)/$', views.city_pins, name='city_pins'),
]
