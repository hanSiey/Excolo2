from django.db import models
from datetime import datetime

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    email = models.EmailField(null=True)
    message = models.CharField(max_length=3000)
    date_sent = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    email = models.EmailField(null=True)
    number_of_guests = models.CharField(max_length=5)
    booking_date = models.DateField()
    date_sent = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.name

class Quote(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    email = models.EmailField(null=True)
    number_of_guests = models.CharField(max_length=5)
    date_sent = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
