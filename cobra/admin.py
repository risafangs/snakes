# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question, Choice


# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'image')
    search_fields = ('id',)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_id_display', 'choice_text', 'choice_type')
    search_fields = ('id',)

    def question_id_display(self, obj):
        return obj.question_id

    question_id_display.short_description = 'Question ID'


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
