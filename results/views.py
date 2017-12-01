from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db import IntegrityError
from django.db.models import Avg, Max
from django.contrib.auth.models import User
from datetime import date
from crispy_forms.helper import FormHelper
from .models import Event, Result, Player
from string import ascii_uppercase
#Added for use with ChartsJs
from django.http import JsonResponse
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response


def todays_date():
    todays_date = date.today()
    today = todays_date.strftime("%Y-%m-%d")
    return today

@login_required
def dashboard(request):
    events = Event.objects.order_by('-date_of_event')
    members = Player.objects.order_by('last_name')
    context = {
        "events" : events,
        "members" : members
    }
    return render(request, 'results/dashboard.html', context)

@login_required
def events(request):
    events = Event.objects.order_by('-date_of_event')
    context = {
        "events" : events
    }
    return render(request, 'results/events.html', context)

@login_required
def members(request):
    members = []
    # loop through the alphabet and create a dicitionairy of each member per letter
    # istartwith is case insensitive search
    for alpha in ascii_uppercase:
        member_list = Player.objects.filter(last_name__istartswith=alpha)
        output = ( alpha, ( member_list ))
        members.append(output)

    context = {
        "members" : members
    }

    return render(request, 'results/members.html', context)

@login_required
def get_event(request,fk):
    event = get_object_or_404(Event,pk=fk)
    result = Result.objects.filter(event_id=fk).order_by('event_rank')
    events = Event.objects.order_by('-date_of_event')
    context = {
            "result": result,
            "event": event,
            "events" : events
             }

    return render(request, 'results/getevent.html', context)

@login_required
def get_player_history(request,pk):
    player = get_object_or_404(Player,id=pk)
    avg_score = Result.objects.filter(player_id=pk).aggregate(Avg('total_score'))
    rds_played = Result.objects.filter(player_id=pk).count()
    history = Result.objects.filter(player_id=pk).order_by('-event__date_of_event')
    handicap_history = Result.objects.filter(player_id=pk).order_by('event__date_of_event')

    #Data values for the Handicap chart
    data_values = []
    for a in handicap_history:
        key_val = (a.event.date_of_event, a.handicap)
        data_values.append(key_val)

    context = {
        "history": history,
        "avg_score" : avg_score,
        "rds_played" : rds_played,
        "player" : player,
        "chart" : data_values,
        "id" : pk,
    }
    return render(request, 'results/getplayerhistory.html', context)

def chart(request,pk):
    # Take the PK, output to the Charting Template and use as the PK
    # for the the API Endpoint when retieving charts
    context = {"id" : pk,}
    return render(request, 'results/chart.html', context )

class ChartData(APIView):
    # Rest API class for returning Charting Data
    authentication_classes = []
    permission_classes = []

    def get(self, request, pk, format=None,):
        data_handicap_date = []
        data_handicap_values = []
        data_performance = []

        # pick up the Primary Key from the URL for use as the API Endpoint
        pk = self.kwargs.get("pk")
        handicap_history = Result.objects.filter(player_id=pk).order_by('event__date_of_event')

        for hc_hist in handicap_history:
            data_handicap_date.append(hc_hist.event.date_of_event)
            data_handicap_values.append(hc_hist.handicap)

        # Retrieve Values for Event Performance, apend them the API endpoint
        data_performance.append(Result.objects.filter(player_id=pk).count())
        data_performance.append(Result.objects.filter(player_id=pk,event_rank=1).count())
        data_performance.append(Result.objects.filter(player_id=pk,event_rank=2).count())
        data_performance.append(Result.objects.filter(player_id=pk,event_rank=3).count())

        # Data for the charts
        data = {
            "handicap_date" : data_handicap_date,
            "handicap_values" : data_handicap_values,
            "performance_labels" : ['Total Events Played','1st Place','2nd Place','3rd Place'],
            "performance_data" : data_performance
        }

        return Response(data)
