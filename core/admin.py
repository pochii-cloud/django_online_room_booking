from django.contrib import admin

# Register your models here.
from core.models import Rooms,Contacts

admin.site.register(Rooms)
admin.site.register(Contacts)
