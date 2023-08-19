from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import ArticleCreateView, ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, \
    toggle_activity

app_name = BlogConfig.name

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('', cache_page(60)(ArticleListView.as_view()), name='list'),
    path('view/<int:pk>', ArticleDetailView.as_view(), name='view'),
    path('edit/<int:pk>', ArticleUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
    path('publish/<int:pk>', toggle_activity, name='toggle_activity'),
]