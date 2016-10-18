# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	# question_image later
	 

class Choice(models.Model):
	choice_text = models.CharField(max_length=200)
	destination = models.CharField(max_length=200)
	question_id = models.ForeignKey('Question', related_name='choices')