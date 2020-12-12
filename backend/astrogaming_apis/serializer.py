from rest_framework import serializers
from .models import Astro


class AstroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Astro
        fields = "__all__"


