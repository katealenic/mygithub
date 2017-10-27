from django import forms
from django.forms import Textarea

from main.models import News


class NewForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'body','publish',)
        widgets = {
            'body': Textarea(attrs={'cols': 40, 'rows': 10}),
        }
