from django.conf.urls import url
from . import views

#  Name the App
app_name = 'society_admin'

urlpatterns = [
    url(r'^createevent/', views.create_event, name='create_event'),
    url(r'^createplayer/', views.create_player, name='create_player'),
]
