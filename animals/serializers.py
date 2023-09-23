from .models import Animal
from rest_framework import serializers

## Class TodoSerializer is a subclass of serializers.HyperlinkedModelSerializer.
## For serializing and deserializing data into representations such as json.
class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    ## Meta class is for configuring the TodoSerializer class.
    class Meta:
        # model to serialize
        model = Animal
        # fields to show in json
        fields = ('id', 'species_name', 'description', 'habitat', 'conservation_status', 'population', 'image')