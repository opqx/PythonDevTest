from clients.models import Contact
from clients.serializers import ContactSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import requests

serializer = ContactSerializer(Contact.objects.all(), many=True)
serializer.data

content = JSONRenderer().render(serializer.data)
content


r = requests.get('https://jsonplaceholder.typicode.com/users')
r.json()

stream = BytesIO(r.content)
data = JSONParser().parse(stream)
serializer = ContactSerializer(data=data)

serializer.is_valid() # todo opqx невалидные данные изменить структуру

serializer.validated_data
serializer.save()


'''
contact
- company
-- address [tree]
'''
