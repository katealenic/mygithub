from django import forms

from main.models import Developer, Wiki, Discussions, Comment


class PersonForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ('peopl','publish',)


class WikiForm(forms.ModelForm):
    class Meta:
        model = Wiki
        fields = ('title','txt',)

class DiscusForm(forms.ModelForm):
    class Meta:
        model = Discussions
        fields = ('txt','title',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text','publish',)