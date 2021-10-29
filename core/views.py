from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, FormView

from core.forms import ContactForm
from core.models import Rooms


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
