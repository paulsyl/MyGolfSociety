from django.conf.urls import url
from . import views
#  Name the App
app_name = 'results'

urlpatterns = [
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^createevent/', views.create_event, name='create_event'),
]
