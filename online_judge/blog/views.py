from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .forms import PostModelForm
from .models import Post 
from django.urls import reverse_lazy
# Create your views here.



class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']	
	paginate_by = 3

class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 3

	def get_queryset(self): 
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

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

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	template_name = 'blog/post_create.html'
	form_class = PostModelForm
	queryset = Post.objects.all()

	def form_valid(self, form): 
		form.instance.author = self.request.user
		#print(form.cleaned_data)
		return super().form_valid(form)

	def test_func(self): 
		post = self.get_object()
		if self.request.user == post.author: 
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post 
	success_url = reverse_lazy('blog-home')
	def test_func(self): 
		post = self.get_object()
		if self.request.user == post.author: 
			return True
		return False






def about(request):
	context = {}
	return render(request, 'blog/about.html', context)


