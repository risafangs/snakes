# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 23:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cobra', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobra.Question')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='cobra.Question')),
            ],
        ),
        migrations.RemoveField(
            model_name='choices',
            name='question_id',
        ),
        migrations.DeleteModel(
            name='Choices',
        ),
    ]