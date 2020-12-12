# Generated by Django 3.1.1 on 2020-09-19 19:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('astrogaming_apis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='astro',
            name='modulename',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='astro',
            name='platform',
            field=models.CharField(max_length=150),
        ),
    ]
