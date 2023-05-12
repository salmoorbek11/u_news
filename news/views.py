from django.views.generic import ListView, DetailView
from .models import News
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class HomePageView(ListView):
    model = News
    template_name = 'home.html'

class NewsDetailView(DetailView):
    model = News
    template_name = "news_detail.html"

class NewsCreateView(CreateView):
    model = News
    template_name = "news_new.html"
    fields = ["title", "author", "body", "created_date", "published_date" ]

class NewsUpdateView(UpdateView):
    model = News
    template_name = "post_edit.html"
    fields = ["title", "body"]

class BlogDeleteView(DeleteView):
    model = News
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")