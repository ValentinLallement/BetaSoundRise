from django import forms
from .models import Pulse

class PulseForm(forms.ModelForm):
    class Meta:
        model = Pulse
        fields = ['title', 'description', 'video', 'tags']