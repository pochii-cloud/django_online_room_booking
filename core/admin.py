from django.contrib import admin

# Register your models here.
from core.models import Rooms, Contacts, Category, Bookedroom

admin.site.register(Rooms)
admin.site.register(Contacts)
admin.site.register(Category)
admin.site.register(Bookedroom)
