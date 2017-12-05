from django.shortcuts import reverse
from django import forms
from django.contrib.auth.models import User
from results.models import Event, Result, Player
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset, Field
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab, FormActions


class LoginForm(forms.ModelForm):

    username = forms.CharField(max_length=75, required=True)
    password = forms.CharField(max_length=75, required=True)

    def __init__(self, *args, **kwargs):
           super(LoginForm, self).__init__(*args, **kwargs)
           self.helper = FormHelper()
           self.helper.form_id = 'id-new-event-form'
           self.helper.form_method = 'POST'
           self.helper.form_class = 'form-horizontal'
           self.helper.label_class = 'col-sm-2'
           self.helper.field_class = 'col-sm-4'
           self.helper.layout = Layout(
                    Field('username', style="color: brown;", placeholder="Username"),
                    Field('password', style="color: brown;", placeholder="Password"),
                    FormActions(Submit('Login', 'Login', css_class='btn-primary'))
           )

    class Meta:
        model = User
        fields = ('username','password')
