from rest_framework import routers, serializers, viewsets

from .models import Season

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class SeasonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Season
        #fields = ('url', 'username', 'email', 'is_staff')

class SeasonUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        
