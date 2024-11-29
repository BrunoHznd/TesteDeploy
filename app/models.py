from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length = 255)

    def _str_(self):
        return f"{self.nome}"

class Produto(models.Model):
    nome = models.CharField(max_length = 255)
    preco = models.DecimalField(max_digits = 10, decimal_places = 2)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)

    def _str_(self):
        return f"Nome: {self.nome}, Preço {self.preco} e categoria {self.categoria}"