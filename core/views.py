from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, FormView, ListView, DetailView

from core.forms import ContactForm
from core.models import *


class BaseView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = Rooms.objects.all()
        return context


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


class EconomicRooms(ListView):
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
        rooms.booked = True
        rooms.save()
        messages.info(request, 'room successfully booked')
        return render(request, 'details.html', {'rooms': rooms})


class UnBookRoom(View):
    def get(self, request, pk):
        rooms = Rooms.objects.get(pk=pk)
        rooms.booked = False
        if rooms.booked is False:
            return HttpResponse("room not booked")
        rooms.save()
        messages.info(request, 'room successfully unbooked')
        return render(request, 'details.html', {'rooms': rooms})