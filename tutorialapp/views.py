from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Tutorial
from .serializers import TutorialSerializer

# Create your views here.


class TutorialView(ModelViewSet):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer
