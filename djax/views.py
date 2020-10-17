from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.shortcuts import render

from djax import forms

# Create your views here.

class AddressView(FormView):
    template_name = 'form.html'
    form_class = forms.AddressForm
    success_url = '/form-data/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)


class AddressDataView(TemplateView):
    template_name = 'form-data-table.html'
