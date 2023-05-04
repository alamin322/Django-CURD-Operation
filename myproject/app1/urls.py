from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('delete/<int:id>/', views.delete_info, name="delete_data"),
    path('update/<int:id>/', views.update_info, name="update_data"),
]