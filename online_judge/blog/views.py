from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostModelForm
from .models import Post 
# Create your views here.



class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post
	#Template name will be defualt : <app>/<model>_<viewtype>/

class PostCreateView(LoginRequiredMixin, CreateView):
	template_name = 'blog/post_create.html'
	form_class = PostModelForm
	queryset = Post.objects.all()

	def form_valid(self, form): 
		form.instance.author = self.request.user
		print(form.cleaned_data)
		return super().form_valid(form)




def about(request):
	context = {}
	return render(request, 'blog/about.html', context)


