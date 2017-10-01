from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db import IntegrityError
from django.contrib.auth.models import User
from . models import Event, Result, Player

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
def create_event(request):
    # Create the event if a POST request is issued
    if request.method == 'POST':
        if request.POST['venue'] and request.POST['event_date']:
            venue = request.POST['venue']
            date_of_event = request.POST['event_date']
            # Check for existence of event prior to making the Model.Save
            event = Event.objects.filter(venue=venue,date_of_event=date_of_event)
            context = {
                "error": 'ERROR: This event on this date has already been created!'
            }

            if event:
                return render(request, 'results/create_event.html', context)
            else:
                Event.objects.create(venue=venue,
                                     date_of_event=date_of_event,
                                     event_type='S')
            context = {
                "success": 'Event Created!'
            }

            return render(request, 'results/create_event.html', context)
        else:
            # Error in the event that the venue and event_Date have not been supplied.
            context = {
                "error": 'ERROR: You must include a Venue and Date to create an Event'
            }
            return render(request, 'results/create_event.html', context)
    else:
        return render(request, 'results/create_event.html')

@login_required
def create_player(request):
    # Create the event if a POST request is issued
    if request.method == 'POST':
        if request.POST['first_name'] and request.POST['last_name']:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            age = request.POST['age']
            date_joined = request.POST['date_joined']
            starting_handicap = request.POST['starting_handicap']
            # Check for existence of player prior to making the Model.Save
            player = Player.objects.filter(first_name=first_name, last_name=last_name)
            context = {
                "error": 'ERROR: This player has already been created!'
            }

            if player:
                return render(request, 'results/create_player.html', context)
            else:
                Player.objects.create(first_name=first_name,
                                      last_name=last_name,
                                      age=age,
                                      date_joined=date_joined,
                                      starting_handicap=starting_handicap
                                      )
            context = {
                "success": 'Player Created!'
            }

            return render(request, 'results/create_player.html', context)
        else:
            # Error in the event that the venue and event_Date have not been supplied.
            context = {
                "error": 'ERROR: You must include a First Name and Last Name to create a Player'
            }
            return render(request, 'results/create_player.html', context)
    else:
        return render(request, 'results/create_player.html')

@login_required
def get_event(request,fk):
    result = Result.objects.filter(event_id=fk).order_by('event_rank')
    event = Event.objects.get(pk=fk)
    context = {
            "result": result,
            "event": event
             }

    return render(request, 'results/getevent.html', context)

@login_required
def get_player_history(request,pk):
    history = Result.objects.filter(player_id=pk).order_by('-event__date_of_event')
    context = {
        "history": history
    }
    return render(request, 'results/getplayerhistory.html', context)
