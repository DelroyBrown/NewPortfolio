from django import forms
from .models import WelcomePageVisitorName

class WelcomePageVisitorNameForm(forms.ModelForm):
    class Meta:
        model = WelcomePageVisitorName
        fields = ['visitors_name']
        widgets = {
            'visitors_name': forms.TextInput(
                attrs={'style': 'text-align: center; border: none;', 'placeholder': ' '}
            )
        }
        labels = {'visitors_name': ''}
