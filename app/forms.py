from django import forms 
from app.models import Produto 

class FormProduto(forms.ModelForm):
    class Meta: 
        model = Produto 
        fields = ("nome", "preco", "categoria")
        