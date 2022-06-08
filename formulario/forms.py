from django import forms
from .models import FormularioModel
from django.forms.widgets import ClearableFileInput


class FormularioModelForm(forms.ModelForm):
    imagem_original = forms.ImageField(widget=ClearableFileInput, required=False)
    imagem_tratada = forms.ImageField(widget=ClearableFileInput, required=False)
    imagem_copilada = forms.ImageField(widget=ClearableFileInput, required=False)

    descricao = forms.CharField(label='Descrição', required=False, widget=forms.Textarea(attrs={
        "cols": 80,
        "rows": 4,

    }))

    class Meta:
        model = FormularioModel
        fields = ['imagem_original', 'valor', 'data', 'descricao', 'imagem_tratada', 'imagem_copilada']
