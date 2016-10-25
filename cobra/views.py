# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from .models import Question, Choice

# Create your views here.

def display_question(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	choices = question.choices
	""" I don't understand what question.choices does or how to pass it a question_id
		I can't say question_id = question_id?
	"""

	context = {
		'fun_question': question,
		'fun_choices': choices
	}
	return render(request, 'index.html', context)