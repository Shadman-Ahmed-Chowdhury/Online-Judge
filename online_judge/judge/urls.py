from django.urls import path
from . import views 

app_name = 'judge'

urlpatterns = [ 
	path("", views.index, name='index'),
]