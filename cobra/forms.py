from django import forms

class SMSQuestionForm(forms.Form):
	to_number = forms.CharField(label='Who to text?', max_length=10)
	message_body = forms.CharField(label='Message body', max_length=140)