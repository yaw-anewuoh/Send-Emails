import imp
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView,TemplateView
from .forms import UserForm

# Create your views here.

class ContactView(FormView):
    template_name='mail/Home.html'
    form_class=UserForm
    success_url=reverse_lazy('mail:Done')

    def form_valid(self,form):
        form.send()
        return super().form_valid(form)

class ContactSuccessView(TemplateView):
    template_name = 'mail/Done.html'

