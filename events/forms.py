from django import forms
from .models import Event, Response

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'start_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'slug': forms.TextInput(attrs={
                'title': 'This field is auto-generated to create a unique URL for the event. Click on it to copy it to the clipboard. Save it and share it with the participants.',
                'style': 'cursor: help;',
                'readonly': 'readonly'
            }),
        }

        

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = '__all__'

