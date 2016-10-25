# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	# question_image later
	def __str__(self):
		return self.question_text
	 

class Choice(models.Model):
	choice_text = models.CharField(max_length=200)
	destination = models.PositiveIntegerField
	question_id = models.ForeignKey('Question', related_name='choices')

	def __str__(self):
		return self.choice_text # how to get it to return foreign key too?
