from django.shortcuts import render
from .models import Question

# Create your views here.
def question_list(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, "core/question_list.html", {"questions": questions})

