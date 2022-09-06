from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm

class NotesForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=['title','description']


class DateInput(forms.DateInput):
    input_type='date'

class AssignmentsForm(forms.ModelForm):
    class Meta:
        model=Assignments
        widgets={'due':DateInput()}
        fields=['subject', 'title', 'description', 'due', 'is_finished']

class DashboardForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Search', 'required': 'true'}),
    max_length=50, label='', required=False)

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['task', 'status']
        labels={
        	'status': 'Is_finished'
        }


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'password1', 'password2']
