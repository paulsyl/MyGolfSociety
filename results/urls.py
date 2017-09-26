from django.conf.urls import url
from . import views
#  Name the App
app_name = 'results'

urlpatterns = [
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^createevent/', views.create_event, name='create_event'),
    url(r'^getevent/(?P<fk>[0-9]+)', views.get_event, name='get_event'),
    #url(r'^getevent/', views.get_event, name='get_event'),
]
