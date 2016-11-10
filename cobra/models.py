# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.question_text

class Choice(models.Model):
	choice_text = models.CharField(max_length=200)
	destination = models.ForeignKey('Question')
	question = models.ForeignKey('Question', related_name='choices')
	
	# here are my choice types:
	link = 'LNK'
	sms = 'SMS'
	email = 'EML'
	braintree = 'BT'
	choice_type_choices = (
	    ('LNK', 'link'), # not sure why I need to make this a tuple
	    ('SMS', 'sms'),
	    ('EML', 'email'),
	    ('BT', 'braintree'),
    )
	choice_type = models.CharField(
		max_length=15,
		choices=choice_type_choices,
		default=link,
	)

	def __str__(self):
		return self.choice_text # how to get it to return foreign key in shell too?


