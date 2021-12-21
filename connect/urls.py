from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('message', views.message, name="message"),
    path('booking', views.booking, name="booking"),
    path('quote', views.quote, name="quote"),

    path('message1', views.message1, name="message1"),
    path('message2', views.message2, name="message2"),
    path('message3', views.message3, name="message3"),


]