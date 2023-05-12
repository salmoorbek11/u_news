from django.urls import path
from news.views import HomePageView, NewsDetailView, NewsCreateView, NewsUpdateView, BlogDeleteView

urlpatterns = [
    path("post/new/", NewsCreateView.as_view(), name="news_new"),
    path("post/<int:pk>/", NewsDetailView.as_view(), name="news_detail"),
    path("post/<int:pk>/edit/", NewsUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
    path('', HomePageView.as_view(), name='home'),
]