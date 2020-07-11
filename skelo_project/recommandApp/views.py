from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TestSerializer

from .models import TestModel

class TestViewSet(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer
