from django.shortcuts import render
from rest_framework import viewsets
from .serializers import mySerializer
from .models import ContactPage



# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    serializer_class=mySerializer
    queryset=ContactPage.objects.all().order_by('id')