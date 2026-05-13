import json
from django.shortcuts import render
from .models import QuizData


def quiz_view(request):
    # Eng oxirgi saqlangan matnni oladi
    last_quiz = QuizData.objects.last()

    # Agar baza bo'sh bo'lsa xato bermasligi uchun
    content = last_quiz.raw_content if last_quiz else "[]"

    context = {
        'questions_raw': content
    }
    return render(request, 'test.html', context)