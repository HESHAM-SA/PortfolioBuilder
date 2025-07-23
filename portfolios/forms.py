# portfolios/forms.py

from django import forms
from .models import TimelineEvent
from .models import Portfolio

class TimelineEventForm(forms.ModelForm):
    class Meta:
        model = TimelineEvent
        fields = [
            'event_type', 
            'title', 
            'company', 
            'description', 
            'event_image',
            'video_url',
            'start_date', 
            'end_date'
        ]
        
        # Add widgets to make the form look better with Bootstrap
        widgets = {
            'event_type': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., University of Tech, TechCorp Inc.'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'event_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'video_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://www.youtube.com/watch?v=...'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        
        help_texts = {
            'end_date': 'Leave this blank for ongoing events (like your current job).'
        }


# portfolios/forms.py

# ... add this new form class ...
class PortfolioEditForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['full_name', 'title', 'bio', 'profile_image', 'email', 'linkedin_url']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'profile_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control'}),
        }