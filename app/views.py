from django.shortcuts import render, redirect
from app.models import Produto
from app.forms import FormProduto
from .serializers import ProdutoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests


#os methodos get e post sao acessados na mesma url , nao precisam do id
@api_view(['GET','POST'])
def getProdutos(request):
    if request.method == 'GET':
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#os methodos getid e put sao em outra pois precisam do id para ver um registro especifico ou alterar
@api_view(['GET','PUT','DELETE'])        
def getProdutoID(request, id_produto):
    try:
        produto = Produto.objects.get(id=id_produto)
    except Produto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
def getAPI(request):
    dadosAPI = requests.get('https://jsonplaceholder.typicode.com/users').json()
    return render(request,'api.html',{'dados':dadosAPI})

#create your views here 
def index(request):
    p = Produto.objects.all()

    formP = FormProduto(request.Post or None)
    if request.Post: 
        if formP.is_valid():
            formP.save()
            return redirect('index')

    return render(request, 'index.html', {'produtos':p, 'form':formP})
