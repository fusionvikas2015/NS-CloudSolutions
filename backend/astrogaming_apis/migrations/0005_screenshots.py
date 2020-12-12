# Generated by Django 3.1.1 on 2020-09-20 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrogaming_apis', '0004_astro_platform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Screenshots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('udid', models.CharField(max_length=100)),
                ('port', models.CharField(max_length=100)),
                ('platform', models.CharField(max_length=150)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
