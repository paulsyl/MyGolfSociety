from django.shortcuts import reverse
from django import forms
from results.models import Event, Result, Player
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset, Field
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab, FormActions



class EventForm(forms.ModelForm):

    venue = forms.CharField(required=True, max_length=100, label="Name of Venue")
    date_of_event = forms.DateField(required=True,label="Event Date", input_formats=['%Y-%m-%d'])

    def __init__(self, *args, **kwargs):
           super(EventForm, self).__init__(*args, **kwargs)
           self.helper = FormHelper()
           self.helper.form_id = 'id-new-event-form'
           self.helper.form_method = 'POST'
           self.helper.form_class = 'form-horizontal'
           self.helper.label_class = 'col-sm-2'
           self.helper.field_class = 'col-sm-4'
           self.helper.layout = Layout(
                    Field('venue', style="color: brown;", placeholder="Venue Name"),
                    Field('date_of_event', style="color: brown", placeholder="YYYY-MM-DD"),
                    FormActions(Submit('Create Event', 'Create Event', css_class='btn-primary'))
           )

    class Meta:
        model = Event
        fields = ('venue', 'date_of_event')

class PlayerForm(forms.ModelForm):

    first_name = forms.CharField(max_length=75, required=True)
    last_name = forms.CharField(max_length=75, required=True)
    starting_handicap = forms.DecimalField(max_digits=3, decimal_places=1, required=True)

    def __init__(self, *args, **kwargs):
           super(PlayerForm, self).__init__(*args, **kwargs)
           self.helper = FormHelper()
           self.helper.form_id = 'id-new-event-form'
           self.helper.form_method = 'POST'
           self.helper.form_class = 'form-horizontal'
           self.helper.label_class = 'col-sm-2'
           self.helper.field_class = 'col-sm-4'
           self.helper.layout = Layout(
                    Field('first_name', style="color: brown;", placeholder="First Name"),
                    Field('last_name', style="color: brown;", placeholder="Last Name"),
                    Field('starting_handicap', style="color: brown;", placeholder="eg, 21.1"),
                    FormActions(Submit('Create Player', 'Create Player', css_class='btn-primary'))
           )

    class Meta:
        model = Player
        fields = ('first_name','last_name', 'starting_handicap')
