from django.urls import path
from watches.views import *
app_name='something'
urlpatterns=[
    path('apple/',apple,name='apple'),
]