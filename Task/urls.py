from django.urls import path
from .views import (
    ClientListAPIView,
    ClientCreateAPIView,
    ClientDetailAPIView,
    ClientUpdateAPIView,
    ClientDeleteAPIView,
    ProjectCreateAPIView,
    ProjectListAPIView,
)

urlpatterns = [
    path('clients/', ClientListAPIView.as_view(), name='client-list'),
    path('clients/create/', ClientCreateAPIView.as_view(), name='client-create'),
    path('clients/<int:pk>/', ClientDetailAPIView.as_view(), name='client-detail'),
    path('clients/<int:pk>/update/', ClientUpdateAPIView.as_view(), name='client-update'),
    path('clients/<int:pk>/delete/', ClientDeleteAPIView.as_view(), name='client-delete'),
    path('clients/<int:pk>/projects/create/', ProjectCreateAPIView.as_view(), name='project-create'),
    path('projects/', ProjectListAPIView.as_view(), name='project-list'),
]
