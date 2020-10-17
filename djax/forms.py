from django import forms
from .models import Address
from django.utils.translation import gettext_lazy as _


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        labels = {
            'address_1': _('Present Address'),
            'address_2': _('Permanent Address'),
            'zip_code': _('Zip'),
        }
        widgets = {
            'email': forms.TextInput(attrs={
                'placeholder': 'Email',
                'required': True,
            }),
            'password': forms.PasswordInput(attrs={
                'required': True,
            }),
            'address_1': forms.TextInput(attrs={
                'label': 'Present Address',
                'placeholder': '1234 Main St',
                'required': True
            }),
            'address_2': forms.TextInput(attrs={
                'placeholder': 'Apartment, studio, or floor',
                'required': True
            }),
            'zip_code': forms.TextInput(attrs={
                'required': True
            }),
            'check_me_out': forms.CheckboxInput(),
        }
