from django.contrib import admin
from app.models import Produto, Categoria

class ProdutoAdmin(admin.ModelAdmin):
    list_diplay = ('nome', 'preco', 'categoria')

# Register your models here.

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria)