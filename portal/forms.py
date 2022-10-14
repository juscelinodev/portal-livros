from django import forms
from portal.models import Autor, Livro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ('nome', 'data_nascimento', 'email')

        widgets = {
            'nome' : forms.TextInput(attrs={'class':'form-control','autofocus':''}),
            'data_nascimento': forms.DateInput(attrs={'class':'form-control'},format='%d/%m/%Y'),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ('titulo', 'subtitulo', 'autor', 'data_lancamento', 'isbn', 'numero_paginas')

        widgets = {
            'titulo' : forms.TextInput(attrs={'class':'form-control','autofocus':''}),
            'subtitulo' : forms.TextInput(attrs={'class':'form-control','autofocus':''}),
            'autor' : forms.Select(attrs={'class':'form-control','autofocus':''}),
            'data_lancamento': forms.DateInput(attrs={'class':'form-control'},format='%d/%m/%Y'),
            'isbn' : forms.TextInput(attrs={'class':'form-control','autofocus':''}),
            'numero_paginas' : forms.NumberInput(attrs={'class':'form-control','autofocus':''}),
            
        }