from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    #rota para api
    path('produtos/',views.getProdutos, name='getProdutos'),
    path('produtos/<int:id_produto>',views.getProdutoID, name='getProdutoID'),
    path('api/',views.getAPI,name='getAPI'),

]
