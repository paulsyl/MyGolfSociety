from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db import IntegrityError
from django.db.models import Avg, Max
from django.contrib.auth.models import User
from datetime import date
from crispy_forms.helper import FormHelper
from results.models import Event, Result, Player
from .forms import EventForm, PlayerForm
from string import ascii_uppercase


def todays_date():
    todays_date = date.today()
    today = todays_date.strftime("%Y-%m-%d")
    return today

@login_required
def create_event(request):

    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():
            event = form.save(commit=False)
            event.venue = form.cleaned_data['venue']
            event.date_of_event = form.cleaned_data['date_of_event']
            event.save

            Event.objects.create(venue=event.venue,
                                 date_of_event=event.date_of_event)

            return redirect('results:events')
    else:
        form = EventForm()

    return render(request, 'society_admin/create_event.html', {"form": form})

@login_required
def create_player(request):

    if request.method == 'POST':
        form = PlayerForm(request.POST)

        if form.is_valid():
            player = form.save(commit=False)
            player.first_name = form.cleaned_data['first_name']
            player.last_name = form.cleaned_data['last_name']
            player.date_joined = todays_date()
            player.starting_handicap = form.cleaned_data['starting_handicap']
            player.save

            # Check to see if the player already exists
            player_check = Player.objects.filter(first_name=player.first_name, last_name=player.last_name)

            if player_check:
                render(request, 'society_admin/create_player.html', {
                                                            "form": form,
                                                            "error": "ERROR: This player has already been created!"
                                                            })
                #  Need to figure out why error message is not returning
            else:
                Player.objects.create(first_name=player.first_name,
                                      last_name=player.last_name,
                                      date_joined=player.date_joined,
                                      starting_handicap=player.starting_handicap)

                return redirect('results:members')
    else:
        form = PlayerForm()

    return render(request, 'society_admin/create_player.html', {"form": form})
