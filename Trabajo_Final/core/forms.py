from django import forms

class FilialForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    sede = forms.CharField(max_length=20)