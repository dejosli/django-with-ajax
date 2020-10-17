from django.views.generic.edit import FormView
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from djax.forms import AddressForm
from .models import Address

# Create your views here.


class AddressView(FormView):
    template_name = 'form-table.html'
    form_class = AddressForm

    def form_valid(self, form):
        return super().form_valid(form)


def address_create_view(request):
    if request.method == 'POST' and request.is_ajax():
        form = AddressForm(request.POST)
        if form.is_valid:
            form.save()
            return JsonResponse({'success': True}, status=200)
    return JsonResponse({'success': False}, status=400)


def address_retrieve_view(request):
    if request.method == 'GET' and request.is_ajax():
        data = serializers.serialize("json", Address.objects.all())
        return JsonResponse({'data': data, 'success': True}, status=200)
    return JsonResponse({'success': False}, status=400)
