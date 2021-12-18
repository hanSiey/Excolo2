from django.contrib import admin
from django.db.models.query_utils import Q
from .models import Contact,Quote,Booking

# Register your models here.

admin.site.register(Contact)
admin.site.register(Quote)
admin.site.register(Booking)