from django.urls import path
from .views import *


urlpatterns = [
    path('create/', create_object, name='create-object'),
    path('view/', view_objects, name='view-objects')
]
