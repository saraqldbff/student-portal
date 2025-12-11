from rest_framework import serializers
from .models import ServiceRequest

# Serializer used to convert the ServiceRequest model to JSON
# and handle validation for API requests
class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        # Include all fields from the model
        fields = '__all__'
        # These fields cannot be modified by the user through the API
        read_only_fields = ['student', 'status', 'created_at', 'updated_at']