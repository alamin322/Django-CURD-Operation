from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.home, name="homepage"),
    path('del/<str:id>', view=views.delete, name="deletepage"),
]
