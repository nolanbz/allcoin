from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import PostCreateForm
from .models import Post

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger



class ListView(ListView):
	template_name = 'posts/coins_list.html'
	paginate_by = 20

	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset = Post.objects.filter(category=slug)
		else:
			queryset = Post.objects.all()
		return queryset.filter(draft=False)

class PostDetailView(DetailView):
	queryset = Post.objects.all()

class PostCreateView(LoginRequiredMixin, CreateView):
	login_url = '/login'
	form_class = PostCreateForm
	template_name = 'posts/create_form.html'

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.owner = self.request.user
		return super(PostCreateView, self).form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
	model = Post
	login_url = '/login'
	form_class = PostCreateForm
	template_name = 'posts/edit_form.html'
