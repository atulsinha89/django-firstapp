# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from models import Question
from django.template import loader
from django.shortcuts import render
from django.http import Http404

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
    'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/details.html', {'question': question})

def results(request):
    return HttpResponse("You are looking at results no - 1")

def vote(request):
    return HttpResponse("You are looking at vote no - 1")