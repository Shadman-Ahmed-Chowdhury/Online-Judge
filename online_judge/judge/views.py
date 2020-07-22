from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Problem
from .forms import ProblemModelForm


from django.urls import reverse_lazy
# Create your views here.

def index(request): 
	return render(request, 'judge/index.html')


class ProblemListView(ListView): 
	model = Problem
	template_name = 'judge/problem_list.html'
	context_object_name = 'problems'
	ordering = ['-created_date']	
	paginate_by = 10

class ProblemDetailView(DetailView):
	template_name = 'judge/problem_detail.html'
	model = Problem

	def get_object(self):
		object = get_object_or_404(Problem, code=self.kwargs['code'])
		return object


class ProblemCreateView(LoginRequiredMixin, CreateView):
	template_name = 'judge/problem_create.html'
	form_class = ProblemModelForm
	queryset = Problem.objects.all()


	def form_valid(self, form): 
		form.instance.author = self.request.user
		print(form.cleaned_data)
		return super().form_valid(form)

class ProblemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	template_name = 'judge/problem_create.html'
	form_class = ProblemModelForm
	queryset = Problem.objects.all()

	def form_valid(self, form): 
		form.instance.author = self.request.user
		#print(form.cleaned_data)
		return super().form_valid(form)

	def test_func(self): 
		post = self.get_object()
		if self.request.user == post.author: 
			return True
		return False

class ProblemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Problem 
	success_url = reverse_lazy('judge:problems-list')
	def test_func(self): 
		post = self.get_object()
		if self.request.user == post.author: 
			return True
		return False


