from rest_framework import serializers
from .models import AstroAutomation



# n the command palette( Ctrl-Shift-P or cmd-Shift-P ) autopep8

class AstroAutomationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstroAutomation
        # fields = ['id', 'platform', 'udid', 'port']
        fields = "__all__"

