from django import forms


from main.models import Developer, Files

class UploadForm(forms.Form):
        file = forms.FileField(widget=forms.FileInput(attrs={'name': 'file'}))


