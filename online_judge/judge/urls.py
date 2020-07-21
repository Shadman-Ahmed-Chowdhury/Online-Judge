from django.urls import path
from . import views 
from .views import ProblemListView, ProblemCreateView, ProblemDetailView

app_name = 'judge'

urlpatterns = [ 
	path("", views.index, name='index'),
	path('problems/', ProblemListView.as_view(), name='problems-list'),
	path('problem/new/', ProblemCreateView.as_view(), name='problem-create'), 
	path('problem/<int:pk>/<code>/', ProblemDetailView.as_view(), name='problem-detail'),
	
]