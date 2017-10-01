from django.conf.urls import url
from . import views
#  Name the App
app_name = 'results'

urlpatterns = [
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^createevent/', views.create_event, name='create_event'),
    url(r'^createplayer/', views.create_player, name='create_player'),
    url(r'^getevent/(?P<fk>[0-9]+)', views.get_event, name='get_event'),
    url(r'^getplayerhistory/(?P<pk>[0-9]+)', views.get_player_history, name='get_player_history'),
]
