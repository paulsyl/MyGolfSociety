from django.conf.urls import url
from . import views
from .views import  ChartData

#  Name the App
app_name = 'results'

urlpatterns = [
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^events/', views.events, name='events'),
    url(r'^members/', views.members, name='members'),
    url(r'^getevent/(?P<fk>[0-9]+)', views.get_event, name='get_event'),
    url(r'^getplayerhistory/(?P<pk>[0-9]+)', views.get_player_history, name='get_player_history'),
    #url(r'^chart', ChartView.as_view(),name='chart'),
    url(r'^chart/(?P<pk>[0-9]+)', views.chart, name='chart'),
    url(r'^api/chart/data/(?P<pk>[0-9]+)/$', ChartData.as_view()),
]
