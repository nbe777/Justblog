from django import forms
from . models import UserProfile
from django.forms import Textarea

class ProfileForm(forms.ModelForm):
    class Meta:
        model= UserProfile
        fields=['bio','profilepic']
        widgets = {
            'bio': Textarea(attrs={'cols': 49, 'rows': 5})
        }
