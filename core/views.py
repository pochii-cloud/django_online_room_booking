from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, FormView, ListView, DetailView

from core.forms import ContactForm
from core.models import *


class BaseView(ListView):
    template_name = 'base.html'
    queryset = Rooms.objects.all()[:8]
    model = Rooms
    context_object_name = 'rooms'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['rooms'] = Rooms.objects.all()
    #     return context


class ContactView(FormView):
    template_name = 'contacts.html'
    form_class = ContactForm
    success_url = '/Success_Message'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Success_Message(TemplateView):
    template_name = 'success_message.html'


class About_page(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


class FirstRooms(ListView):
    template_name = "frooms.html"
    model = Rooms
    context_object_name = 'rooms'


class SecondRooms(ListView):
    template_name = 'srooms.html'
    model = Rooms
    context_object_name = 'rooms'


class SingleRooms(ListView):
    template_name = 'erooms.html'
    model = Rooms
    context_object_name = 'rooms'


class Footer(TemplateView):
    template_name = 'footer.html'


class RoomsDetail(DetailView):
    model = Rooms
    context_object_name = 'rooms'
    template_name = 'details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        rooms = Rooms.objects.filter(pk=self.kwargs.get('pk'))
        return context


class BookRoom(View):
    def get(self, request, pk):
        rooms = Rooms.objects.get(pk=pk)
        if rooms.booked is False:
            rooms.booked = True
            rooms.user = request.user
            rooms.save()
            messages.info(request, 'room successfully booked')
            return redirect('MyroomView')
        else:
            messages.info(request, 'room already booked')
        return render(request, 'details.html', {'rooms': rooms})


class UnBookRoom(View):
    def get(self, request, pk):
        rooms = Rooms.objects.get(pk=pk)
        if rooms.booked is True:
            rooms.booked = False
            rooms.save()
            messages.info(request, 'room successfully unbooked')
        else:
            return HttpResponse('room not booked')
        return render(request, 'details.html', {'rooms': rooms})


class MyroomView(LoginRequiredMixin, View):
    login_url = '/accounts/SignInView/'

    def get(self, request):
        rooms = Rooms.objects.all().filter(user=request.user)
        return render(request, 'myrooms.html', {'rooms': rooms})


class BookedRooms(ListView):
    model = Rooms
    context_object_name = 'bookedrooms'
    template_name = 'bookedrooms.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookedrooms'] = Rooms.objects.filter(booked=True)
        return context


class Categories(ListView):
    template_name = 'categories.html'
    model = Rooms
    context_object_name = 'rooms'
