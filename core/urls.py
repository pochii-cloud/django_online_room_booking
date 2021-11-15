from django.urls import path

from core.views import *

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('RoomsDetail/<int:pk>/', RoomsDetail.as_view(), name='RoomsDetail'),
    path('BookRoom/<int:pk>/', BookRoom.as_view(), name='BookRoom'),
    path('UnBookRoom/<int:pk>/', UnBookRoom.as_view(), name='UnBookRoom'),
    path('FirstRooms/', FirstRooms.as_view(), name='FirstRooms'),
    path('SecondRooms/', SecondRooms.as_view(), name='SecondRooms'),
    path('EconomicRooms/', EconomicRooms.as_view(), name='EconomicRooms'),
    path('ContactView/', ContactView.as_view(), name='ContactView'),
    path('Footer/', Footer.as_view(), name='Footer'),
    path('Success_Message/', Success_Message.as_view(), name='Success_Message'),
    path('About_page/', About_page.as_view(), name='About_page')
]
