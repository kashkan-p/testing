from django.shortcuts import render
from .models import TestModel
import json

# Create your views here.
def create_object(request):
        if request.method=='POST':
            data = request.POST.copy()
            data.pop('csrfmiddlewaretoken', None)
            model = TestModel()
            model.data = json.dumps(data)
            model.save()
            return render(request, 'test_task/success.html')
        else:
            return render(request, 'test_task/create_object.html')

def view_objects(request):
        objects = TestModel.objects.all()
        return render(request, 'test_task/view_objects.html', context={'objects' : objects})
