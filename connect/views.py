from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MessageForm,QuoteForm,BookingForm
# Create your views here.

def index(request):
    message_form = MessageForm()
    quote_form = QuoteForm()
    booking_form = BookingForm()

    forms = {
        'message_form':message_form,
        'quote_form': quote_form,
        'booking_form': booking_form,
    }
    return render(request, "index.html", forms)

def quote(request):
    if request.method == 'POST':
        quote_form = QuoteForm(request.POST)
        if quote_form.is_valid():
            quote_form.save()
            return redirect('/')
        else:
            messages.info(request, "Enter valid information")
            return redirect('/')
    else:
        pass

def message(request):
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            message_form.save()
            return redirect('/')
        else:
            messages.info(request, "Enter valid information")
            return redirect('/')
    else:
        pass

def booking(request):
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking_form.save()
            return redirect('/')
        else:
            messages.info(request, "Enter valid information")
            return redirect('/')
    else:
        pass
