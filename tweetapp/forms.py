from django import forms
from django.forms import ModelForm
from tweetapp.models import Tweet

class AddTweetForm(forms.Form):
    message_input = forms.CharField(
        label="message",
        max_length=100,
        widget=forms.Textarea(attrs={
            'class':'tweetmessage',
            'rows':8
            })
        )
    
class AddTweetModelForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ["username","message"]
