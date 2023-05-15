from django.shortcuts import render
from .models import Olympics
from .serializers import MedSerializer
from json import dumps

# Create your views here.

def home(request):
    item = Olympics.objects.all()
    print(item)
    temp = MedSerializer(item, many = True)
    # print(temp.data)
    dataJSON = dumps(temp.data)
    print(dataJSON)
    return render(request, 'test6/index.html', {'item':dataJSON})
