from .models import Animal
from rest_framework import serializers


class AnimalSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        # model to serialize
        model = Animal
        # fields to show in json
        fields = ('id', 'species_name', 'description', 'habitat', 'conservation_status', 'population', 'image')