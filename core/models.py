from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Rooms(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    booked = models.BooleanField(default=False)
    capacity = models.PositiveIntegerField()
    image = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Rooms'


class Contacts(models.Model):
    username = models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField()
    message = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "contacts"

    def __str__(self):
        return self.username
