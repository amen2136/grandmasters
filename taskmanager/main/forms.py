from dataclasses import fields
from django import forms
from .models import News
from .models import Todo
from django.forms import ModelForm, TextInput, Textarea

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ["title","preview", "textNews"]
        widgets = {
                "title": TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': "Type title of news"
                }),
                "preview": TextInput(attrs={
                    'class' : 'form-control',
                    'placeholder' :  "Type preview of news"
                }),
                "textNews": Textarea(attrs={
                    'class' : 'form-control',
                    'placeholder':  "Type text of news"
                }),
            }

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields ="__all__"
        


        # {
        #     "title": TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': "type title"
        # }),
        #     "task": Textarea(attrs={
        #         'class': 'form-control',
        #         'placeholder': "type description"
        # }),  
        # }