from django.shortcuts import render
from .models import Question
from .forms import QuestionForm, AnswerForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.
def question_list(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, "core/question_list.html", {"questions": questions})

@login_required
def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('question_list')
    else:
        form = QuestionForm()
    return render(request, 'core/question_form.html', {'form': form})

def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = question.answers.all()
    form = AnswerForm()
    return render(request, 'core/question_detail.html', {
        'question': question,
        'answers': answers,
        'form': form
    })

@login_required
def post_answer(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.isValid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = question
            answer.save()
    
    return redirect('question_detail', question_id = question_id)