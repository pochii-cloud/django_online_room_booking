from django.urls import path

from accounts.views import RegisterView, loginview, LogoutView

urlpatterns = [
    path('RegisterView/', RegisterView.as_view(), name='RegisterView'),
    path('SignInView/', loginview, name='SignInView'),
    path('LogoutView/', LogoutView.as_view(), name='LogoutView'),
]
