from django import forms

# creating a form
class LoginForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50)

class DatosForm(forms.Form):
    Foto = forms.URLField()
    Título = forms.CharField(max_length=50)
    Descripción = forms.CharField(max_length=500)
    Tags = forms.CharField(max_length=500)
    URL_github= forms.URLField()

