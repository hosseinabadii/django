from django.urls import path
from . import views

urlpatterns = [
    path('pages/', views.show_objects )
]