from django.forms import ModelForm, TextInput, EmailInput
from .models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
