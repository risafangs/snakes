# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from .forms import SMSQuestionForm
from django.views.generic.edit import FormView 
from django.urls import reverse_lazy
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

class SMSQuestion(FormView):
	form_class = SMSQuestionForm
	template_name = 'smsquestion.html'
	success_url = reverse_lazy('smsquestion')

"""
	def form_valid(self, form):
		account_sid = "AC007ffbc7fa49cdc774c904ecf0ad4dfd"
		auth_token = os.getenv('TWILIO_TOKEN')

		print TWILIO_TOKEN

		client = TwilioRestClient(account_sid, auth_token)

		message = client.messages.create(to="+17084464335", from_="+12023350157 ",
		body="There are snakes here!")

		return super(ContactView, self).form_valid(form)
		"""
