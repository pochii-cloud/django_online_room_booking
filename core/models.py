from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Rooms(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    name = models.CharField(max_length=100)
    booked = models.BooleanField(default=False)
    capacity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='static/images/rooms', blank=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Rooms'


class Bookedroom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    rooms = models.ForeignKey(Rooms, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "USER:" + str(self.user) + "->" + str(self.rooms.name)

    class Meta:
        verbose_name_plural = 'BookedRooms'


class Contacts(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    message = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "contacts"

    def __str__(self):
        return self.username
