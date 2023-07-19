

from django.shortcuts import render
from .models import Question
from django.shortcuts import get_object_or_404, render


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    for i in latest_question_list:
        print(i,"++++++++++++++++")
    context = {"latest_question_list": latest_question_list}
    return render(request, "index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "detail.html", {"question": question})
    