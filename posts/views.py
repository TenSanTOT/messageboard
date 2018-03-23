from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date']

class Write(CreateView):
    model = Post
    template_name = 'posts/write.html'
    fields = ['text','name']
    success_url = reverse_lazy('url_name_home')
