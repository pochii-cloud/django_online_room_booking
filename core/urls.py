from django.urls import path

from core.views import BaseView, ContactView, Success_Message

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('ContactView/', ContactView.as_view(), name='ContactView'),
    path('Success_Message/', Success_Message.as_view(), name='Success_Message')
]
