from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db import IntegrityError
from django.contrib.auth.models import User
from . models import Event

def dashboard(request):
    events = Event.objects.order_by('-date_of_event')
    return render(request, 'results/dashboard.html', {'events': events})

def create_event(request):
    # Create the event if a POST request is issued
    if request.method == 'POST':
        if request.POST['venue'] and request.POST['event_date']:
            venue = request.POST['venue']
            date_of_event = request.POST['event_date']
            # Check for existence of event prior to making the Model.Save
            event = Event.objects.filter(venue=venue,date_of_event=date_of_event)
            if event:
                return render(request, 'results/create_event.html', {'error': 'ERROR: This event on this date has already been created!'})
            else:
                Event.objects.create(venue=venue,
                                     date_of_event=date_of_event,
                                     event_type='S')

            # ********  Need to add uniqueness and add drop down for the event Type

            return render(request, 'results/create_event.html', {'success': 'Event Created!'})
        else:
            # Error in the event that the venue and event_Date have not been supplied.
            return render(request, 'results/create_event.html', {'error': 'ERROR: You must include a Venue and Date to create an Event'})
    else:
        return render(request, 'results/create_event.html')
