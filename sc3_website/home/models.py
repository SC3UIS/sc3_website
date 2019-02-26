from django.db import models

from wagtail.core.models import Page
from .forms import ContactForm


class HomePage(Page):
    
    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['form'] = ContactForm
        return context
