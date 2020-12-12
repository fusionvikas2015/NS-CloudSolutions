from django.db import models

# Create your models here.
class Astro(models.Model):
    udid =models.CharField(max_length=100)
    port = models.CharField(max_length=100)
    modulename = models.CharField(max_length=150)
    platform = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.udid

