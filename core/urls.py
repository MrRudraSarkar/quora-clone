from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name="question_list"),
    path('ask/', views.question_create, name='question_create')
]