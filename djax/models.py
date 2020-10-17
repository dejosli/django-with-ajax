from django.db import models

# Create your models here.

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

class Address(models.Model):
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2, choices=STATES)
    zip_code = models.CharField(max_length=5)
    check_me_out = models.BooleanField(default=False)

    def __str__(self):
        return (self.email)