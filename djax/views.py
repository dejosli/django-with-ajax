from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from djax.forms import AddressForm
from .models import Address

# Create your views here.


class AddressView(FormView):
    template_name = 'form-table.html'
    form_class = AddressForm
    success_url = '/form-data/'

    def form_valid(self, form):
        return super().form_valid(form)


def address_create_view(request):
    if request.method == 'POST' and request.is_ajax():
        form = AddressForm(request.POST)
        if form.is_valid:
            form.save()
            return JsonResponse({'success': True}, status=200)
    return JsonResponse({'success': False}, status=400)

