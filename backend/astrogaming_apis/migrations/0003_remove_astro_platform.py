# Generated by Django 3.1.1 on 2020-09-19 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('astrogaming_apis', '0002_auto_20200919_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='astro',
            name='platform',
        ),
    ]
