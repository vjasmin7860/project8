from django.urls import path
from web.views import *
app_name='something'
urlpatterns=[
    path('kishore/',kishore,name='kishore'),
]