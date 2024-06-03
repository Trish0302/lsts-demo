from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("learning_content", views.learning_content),
    path("implementation", views.implementation),
    path("pdf_viewer", views.pdf_viewer),
]