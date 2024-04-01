from django.urls import path
from sql.views import *
app_name='nothing'
urlpatterns=[
    path('greeshma/',greeshma,name='greeshma'),
]