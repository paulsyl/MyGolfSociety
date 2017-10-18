from django.shortcuts import reverse
from django import forms
from .models import Event, Player
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab

class EventForm(forms.ModelForm):

    venue = forms.CharField(required=True, max_length=100, label="Name of Venue")
    date_of_event = forms.DateField(required=True)

    def __init__(self, *args, **kwargs):
           super(EventForm, self).__init__(*args, **kwargs)
           self.helper = FormHelper()
           self.helper.form_id = 'id-new-event-form'
           self.helper.form_method = 'POST'
           self.helper.form_class = 'form-horizontal'
           self.helper.form_action = 'create_event'
           self.helper.add_input(Submit('Create Event', 'Create Event'))
           self.helper.layout = Layout(
                    Field('venue', style="color: brown;", placeholder="Venue Name"),
                    Field('date_of_event', style="color: brown", placeholder="YYYY-MM-DD")
           )

    class Meta:
        model = Event
        fields = ('venue', 'date_of_event')

class PlayerForm(forms.ModelForm):

    first_name = forms.CharField(max_length=75, required=True)
    last_name = forms.CharField(max_length=75, required=True)
    date_joined = forms.DateField()
    starting_handicap = forms.DecimalField(max_digits=3, decimal_places=1, required=True)

    def __init__(self, *args, **kwargs):
           super(PlayerForm, self).__init__(*args, **kwargs)
           self.helper = FormHelper()
           self.helper.form_id = 'id-new-event-form'
           self.helper.form_method = 'POST'
           self.helper.form_class = 'form-horizontal'
           self.helper.form_action = 'create_player'
           self.helper.add_input(Submit('Create Player', 'Create Player'))

    class Meta:
        model = Player
        fields = ('first_name','last_name', 'date_joined', 'starting_handicap')
