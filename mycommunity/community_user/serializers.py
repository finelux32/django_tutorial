from rest_framework import serializers
from .models import CommunityUser


class CommunityUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityUser
        fields = '__all__'


