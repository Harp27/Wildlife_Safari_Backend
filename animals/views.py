
from .models import Animal
from rest_framework import viewsets, permissions
from .serializers import AnimalSerializer

class AnimalViewSet(viewsets.ModelViewSet):
    
    queryset = Animal.objects.all()
   
    serializer_class = AnimalSerializer
  
    permission_classes = [permissions.AllowAny]