from django import forms
from django.forms import Textarea


class SMSForm(forms.Form):
    to_number = forms.RegexField(regex=r'^\+\d{9,16}$', label='Who to text?', error_messages={
        "invalid": "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."})
    message_body = forms.CharField(label='Message body', widget=Textarea, max_length=140)


class EmailForm(forms.Form):
    to_email = forms.CharField(label='Recipient Email', max_length=140)
    from_email = forms.CharField(label='Your Email', max_length=140)
    message_body = forms.CharField(label='Message', widget=Textarea, max_length=500)

