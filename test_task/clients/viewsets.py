from rest_framework import viewsets  
from .models import Contact
from .serializers import ContactSerializer

from rest_framework import routers  


class ContactViewSet(viewsets.ModelViewSet):  
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


api_router = routers.SimpleRouter()  
api_router.register('contact', ContactViewSet) 
