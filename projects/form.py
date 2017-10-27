from authomatic.core import User
from django import forms


from main.models import Project, Wiki, Developer, Manager
from main.models import Project


class PostForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title','publish',)

class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ('name',)