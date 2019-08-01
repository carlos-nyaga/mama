from rest_framework import serializers
from .models import Attendee

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = ('first_name', 'middle_name', 'last_name',
            'phone_number', 'email', 'ticket', 'created_at', 'updated_at')