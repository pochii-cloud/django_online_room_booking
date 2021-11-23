from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView

from core.forms import RegisterForm


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('SignInView')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # class SignInView(View):


def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base')
        else:
            messages.info(request, 'username OR password incorrect')
    return render(request, 'login.html')


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('SignInView')
