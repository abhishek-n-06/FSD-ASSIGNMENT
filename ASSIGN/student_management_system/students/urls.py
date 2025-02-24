from django.urls import path
from .views import StudentListView, StudentDetailView, StudentUpdateView, StudentDeleteView

urlpatterns = [
    path('', StudentListView.as_view(), name='student-list'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('<int:pk>/edit/', StudentUpdateView.as_view(), name='student-edit'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
]

