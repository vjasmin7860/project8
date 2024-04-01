from django.urls import path
from jewellery.views import *
app_name='anything'
urlpatterns=[
    path('rings/',rings,name='rings')
]