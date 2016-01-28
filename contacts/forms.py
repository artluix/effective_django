from django import forms
from django.core.exceptions import ValidationError

from .models import Contact


class ContactForm(forms.ModelForm):
    
    confirm_email = forms.EmailField(
            label='Confirm email', required=True)


    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            email = kwargs['instance'].email
            kwargs.setdefault('initial', {})['confirm_email'] = email

        return super().__init__(*args, **kwargs)

    def clean(self):
        if (self.cleaned_data.get('email') != 
                self.cleaned_data.get('confirm_email')):
            raise ValidationError('Email addresses must match.')
            
        return self.cleaned_data
            
