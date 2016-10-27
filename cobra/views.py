# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from .models import Question, Choice

# Create your views here.

def display_question(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	choices = question.choices.all()

	context = {
		'fun_question': question,
		'fun_choices': choices
	}
	return render(request, 'index.html', context)