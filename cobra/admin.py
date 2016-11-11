# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','image')
    search_fields = ('id',)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id','question','destination','choice_type')
    search_fields = ('id',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
