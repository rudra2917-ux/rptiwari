import re

from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'phone', 'email', 'company', 'location', 'capacity_tpd', 'service',
                  'project_stage', 'machinery', 'preferred_contact', 'message']
        widgets = {
            'preferred_contact': forms.RadioSelect(attrs={'class': 'radio-pills'}),
            'capacity_tpd': forms.NumberInput(attrs={'placeholder': 'e.g. 100', 'min': 1, 'max': 5000}),
            'name': forms.TextInput(attrs={'placeholder': 'Your full name', 'autocomplete': 'name'}),
            'phone': forms.TextInput(attrs={'placeholder': '10-digit mobile number', 'autocomplete': 'tel', 'inputmode': 'tel'}),
            'email': forms.EmailInput(attrs={'placeholder': 'you@example.com (optional)', 'autocomplete': 'email'}),
            'company': forms.TextInput(attrs={'placeholder': 'Mill / company name (optional)'}),
            'location': forms.TextInput(attrs={'placeholder': 'e.g. Varanasi, Uttar Pradesh'}),
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Tell us about your plant, capacity (TPD) and what you need help with…'}),
        }
        labels = {'service': 'How can we help?', 'project_stage': 'Project stage'}

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        digits = re.sub(r'\D', '', phone)
        if len(digits) < 10 or len(digits) > 13:
            raise forms.ValidationError('Please enter a valid mobile number.')
        return phone
