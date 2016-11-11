# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from .forms import ChoiceForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse
from .models import Question, Choice
from twilio.rest import TwilioRestClient
import os

# Create your views here.

def display_question(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	choices = question.choices.all()

	context = {
		'fun_question': question,
		'fun_choices': choices
	}
	return render(request, 'hello.html', context)

class ChoiceFormView(FormView):
	form_class = ChoiceForm
	template_name = 'choice.html'
	success_url = reverse_lazy('choice')

	def form_valid(self, form):
		# client = TwilioRestClient(account='AC007ffbc7fa49cdc774c904ecf0ad4dfd', token='meow')
		return super(ChoiceFormView, self).form_valid(form) # returns to self

	def get_context_data(self):
		context = super(ChoiceFormView, self).get_context_data()
		choice = Choice.objects.get(pk=self.kwargs['choice_id'])
		context['choice'] = choice
		return context

	def get_success_url(self):
		choice = Choice.objects.get(pk=self.kwargs['choice_id'])
		next_page = reverse('display_question', kwargs={'question_id': choice.destination_id})
		return next_page
