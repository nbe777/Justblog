from django import forms
from . models import BlogModel,CommentModel
from django.forms import Textarea

class BlogForm(forms.ModelForm):
    class Meta:
        model= BlogModel
        fields=['title','subtitle','blog_content','image']
        widgets = {
            'blog_content': Textarea(attrs={'cols': 40, 'rows': 5}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model= CommentModel
        fields=['rating','comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 5}),
        }
