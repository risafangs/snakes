from django import forms


class ChoiceForm(forms.Form):
	to_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label='Who to text?', error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
	message_body = forms.CharField(label='Message body', max_length=140)
