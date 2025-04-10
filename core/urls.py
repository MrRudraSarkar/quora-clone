from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.question_list, name="question_list"),
    path('ask/', views.post_question, name='post_question'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('question/<int:question_id>/answer', views.post_answer, name='post_answer'),
    path('answer/<int:answer_id>/like/', views.like_answer, name='like_answer'),

    #Authentication
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='question_list'), name = 'logout'),
]