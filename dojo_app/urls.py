from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('form_dojo', views.form_dojo),
    path('form_ninja', views.form_ninja),
    path('dojo_remove', views.dojo_remove),
]