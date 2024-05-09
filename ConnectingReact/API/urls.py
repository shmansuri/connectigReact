from django.urls import path,include
from rest_framework import routers
from .views import ContactViewSet

ru=routers.DefaultRouter()
ru.register(r'contact', ContactViewSet)

urlpatterns = [
    path('',include(ru.urls))
]
