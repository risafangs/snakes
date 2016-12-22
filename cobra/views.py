# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.conf import settings
from .forms import SMSForm, EmailForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy, reverse
from .models import Question, Choice
from twilio.rest import TwilioRestClient
import sendgrid
import os
from sendgrid.helpers.mail import *
import braintree


# Create your views here.

def display_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choices.all()
    choice_type = Choice.choice_type

    context = {
        'fun_question': question,
        'fun_choices': choices,
        'choice_type': choice_type
    }
    return render(request, 'hello.html', context)


class SMSFormView(FormView):
    form_class = SMSForm
    template_name = 'choice.html'

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        client = TwilioRestClient(account=settings.TWILIO_ACCOUNT_ID,
                                  token=settings.TWILIO_TOKEN)
        client.messages.create(to=cleaned_data['to_number'], from_="+12023350157",
                               body=cleaned_data['message_body'])

        return super(SMSFormView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SMSFormView, self).get_context_data(**kwargs)
        choice = Choice.objects.get(pk=self.kwargs['choice_id'])
        context['choice'] = choice
        return context

    def get_success_url(self):
        choice = Choice.objects.get(pk=self.kwargs['choice_id'])
        next_page = reverse('display_question', kwargs={'question_id': choice.destination_id})
        return next_page


class EmailFormView(FormView):
    form_class = EmailForm
    template_name = 'choice.html'

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)
        from_email = Email(cleaned_data['from_email'])
        subject = "Hello World from the the fun world of snakes!"
        to_email = Email(cleaned_data['to_email'])
        content = Content("text/plain", cleaned_data['message_body'])
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        return super(EmailFormView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EmailFormView, self).get_context_data(**kwargs)
        choice = Choice.objects.get(pk=self.kwargs['choice_id'])
        context['choice'] = choice
        return context

    def get_success_url(self):
        choice = Choice.objects.get(pk=self.kwargs['choice_id'])
        next_page = reverse('display_question', kwargs={'question_id': choice.destination_id})
        return next_page


class PaymentFormView(TemplateView):
    template_name = 'payment.html'

    braintree.Configuration.configure(
        braintree.Environment.Sandbox,
        settings.BT_MERCHANT_ID,
        settings.BT_PUBLIC_KEY,
        settings.BT_PRIVATE_KEY
    )

    def get_context_data(self, **kwargs):
        context = super(PaymentFormView, self).get_context_data(**kwargs)
        choice = Choice.objects.get(pk=self.kwargs['choice_id'])
        context['choice'] = choice
        return context

    def get(self, request, *args, **kwargs):
        print request.GET
        if 'payment_method_nonce' in request.GET:
            client_nonce = request.GET['payment_method_nonce']
            result = braintree.Transaction.sale({
                "amount": "7.77",
                "payment_method_nonce": client_nonce,
                "options": {
                    "submit_for_settlement": True
                }
            })

            choice = Choice.objects.get(pk=self.kwargs['choice_id'])
            next_page = reverse('display_question', kwargs={'question_id': choice.destination_id})
            return HttpResponseRedirect(next_page)

        else:
            pass
        return super(PaymentFormView, self).get(request, *args, **kwargs)