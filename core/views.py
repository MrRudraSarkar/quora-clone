from django.shortcuts import render
from .models import Question
from .forms import QuestionForm
from django.shortcuts import redirect

# Create your views here.
def question_list(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, "core/question_list.html", {"questions": questions})

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question_list')
    else:
        form = QuestionForm()
    return render(request, 'core/question_form.html', {'form': form})