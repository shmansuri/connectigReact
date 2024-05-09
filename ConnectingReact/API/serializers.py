from rest_framework import serializers
from .models import ContactPage
 
class mySerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactPage
        fields=('id','name','email','phone','company', 'company_website','services', 'describe','term')