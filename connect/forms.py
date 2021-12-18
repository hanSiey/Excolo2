from django import forms
from .models import *

class MessageForm(forms.ModelForm):
    name = forms.CharField(max_length=15, widget=forms.TextInput(
        attrs = {
            'class': 'form-input', 
            'id': 'name',
            'type': 'text',
            'name': 'name',
            'placeholder': 'Your name...',
            'data-constraints': '@Required',
        }
    ))
    surname = forms.CharField(max_length=15, widget=forms.TextInput(
        attrs = {
            'class': 'form-input',
            'id': 'surname', 
            'type': 'text',
            'name': 'surname',
            'placeholder': 'Your surname...',
            'data-constraints': '@Required',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs = {
            'class': 'form-input',
            'id': 'email', 
            'type': 'email',
            'name': 'email',
            'placeholder': 'Your email...',
            'data-constraints': '@Required',
        }
    ))
    message = forms.CharField(max_length=3000, widget=forms.Textarea(
        attrs = {
            'class': 'form-input',
            'id': 'message', 
            'type': 'text',
            'name': 'message',
            'placeholder': 'Your message...',
            'data-constraints': '@Required',
        }
    ))
    class Meta:
        model = Contact
        fields = '__all__'

class BookingForm(forms.ModelForm):
    name = forms.CharField(max_length=15, widget=forms.TextInput(
        attrs = {
            'class': 'form-input',
            'id': 'name', 
            'type': 'text',
            'name': 'name',
            'placeholder': 'Your name...',
            'data-constraints': '@Required',
        }
    ))
    surname = forms.CharField(max_length=15, widget=forms.TextInput(
        attrs = {
            'class': 'form-input',
            'id': 'surname', 
            'type': 'text',
            'name': 'surname',
            'placeholder': 'Your surname...',
            'data-constraints': '@Required',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs = {
            'class': 'form-input',
            'id': 'email', 
            'type': 'email',
            'name': 'email',
            'placeholder': 'Your email...',
            'data-constraints': '@Required',
        }
    ))
    number_of_guests = forms.CharField(max_length=5, widget=forms.TextInput(
        attrs = {
            'class': 'form-input',
            'id': 'guests', 
            'type': 'text',
            'name': 'guests',
            'placeholder': 'No. Guests...',
            'data-constraints': '@Required',
        }
    ))
    booking_date = forms.DateField(widget=forms.DateInput(
        attrs = {
            'class': 'form-input',
            'id': 'date', 
            'type': 'date',
            'name': 'date',
            'data-constraints': '@Required',
        }
    ))
    class Meta:
        model = Booking
        fields = '__all__'

class QuoteForm(forms.ModelForm):
    name = forms.CharField(max_length=15, widget=forms.TextInput(
        attrs = {
            'class': 'form-input',
            'id': 'name', 
            'type': 'text',
            'name': 'name',
            'placeholder': 'Your name...',
            'data-constraints': '@Required',
        }
    ))
    surname = forms.CharField(max_length=15, widget=forms.TextInput(
        attrs = {
            'class': 'form-input',
            'id': 'surname', 
            'type': 'text',
            'name': 'surname',
            'placeholder': 'Your surname...',
            'data-constraints': '@Required',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs = {
            'class': 'form-input',
            'id': 'email', 
            'type': 'email',
            'name': 'email',
            'placeholder': 'Your email...',
            'data-constraints': '@Required',
        }
    ))
    number_of_guests = forms.CharField(max_length=5, widget=forms.TextInput(
        attrs = {
            'class': 'form-input',
            'id': 'guests', 
            'type': 'text',
            'name': 'surname',
            'placeholder': 'No. Guests...',
            'data-constraints': '@Required',
        }
    ))
    class Meta:
        model = Quote
        fields = '__all__'