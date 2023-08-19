from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import DeleteView

from client.apps import ClientConfig
from client.views import ClientListView, ClientCreateView, ClientUpdateView, ClientDetailView, ClientDeleteView

app_name = ClientConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='list'),
    path('create/', ClientCreateView.as_view(), name='create'),
    path('edit/<int:pk>', ClientUpdateView.as_view(), name='edit'),
    path('view/<int:pk>', ClientDetailView.as_view(), name='view_client'),
    path('delete/<int:pk>', ClientDeleteView.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)