# Generated by Django 3.1.1 on 2020-10-17 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djax', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.CharField(max_length=5),
        ),
    ]
