from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name="question_list"),
    path('ask/', views.post_question, name='post_question'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('question/<int:question>/answer', views.post_answer, name='post_answer')
]