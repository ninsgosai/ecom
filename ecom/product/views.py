from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from .models import product
from user.models import user
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
# Create your views here.
def products(request):
    if 'user_id' in request.session and request.session['user_id']:
        products = product.objects.all() 
        return render(request,"products.html",{'products':products})
    else:
        return redirect('home')

@api_view(['POST'])
def list_products(request):
    data = {}
    if 'email' in request.POST and 'password' in request.POST and request.POST['email'] and request.POST['password']:
        if user.objects.filter(email=request.POST['email'],password=request.POST['password']).exists():
            products = product.objects.filter()
            qs_json = serializers.serialize('json', products)
            data = {'error':'0','products' : qs_json}
        else:
            data = {'error':'1','products' : 'Unauthorised User'}
    else:
        data = {'error':'2','data':'Please use email and password to view this products'}
    return JsonResponse(data)

@api_view(['POST'])
def add_products(request):
    data = {}
    if 'email' in request.POST and 'password' in request.POST and request.POST['email'] and request.POST['password']:
        if user.objects.filter(email=request.POST['email'],password=request.POST['password']).exists():
            if 'name' in request.POST and 'price' in request.POST and 'SKU' in request.POST and 'description' in request.POST and 'image' in request.FILES:
                products = product(name = request.POST['name'],price = request.POST['price'],SKU = request.POST['SKU'],description = request.POST['description'],image = request.FILES['image'])
                products.save()
                data = {'error':'3','data':'Product Added'}
            else:
                data = {'error':'4','data':'Please Add All details for Product'}
        else:
            data = {'error':'1','products' : 'Unauthorised User'}
    else:
        data = {'error':'2','data':'Please use email and password to add new products'}
    return Response(data)

@api_view(['POST'])
def edit_products(request):
    data = {}
    if 'email' in request.POST and 'password' in request.POST and request.POST['email'] and request.POST['password']:
        if user.objects.filter(email=request.POST['email'],password=request.POST['password']).exists():
            if 'pk' in request.POST:
                if product.objects.filter(id=request.POST['pk']).exists():
                    if 'name' in request.POST and 'price' in request.POST and 'SKU' in request.POST and 'description' in request.POST and 'image' in request.FILES and request.POST['name'] and request.POST['price'] and request.POST['SKU'] and request.POST['description'] and request.FILES['image']:
                        products = product.objects.get(id=request.POST['pk'])

                        products.name = request.POST['name']
                        products.price = request.POST['price']
                        products.SKU = request.POST['SKU']
                        products.description = request.POST['description']
                        products.image = request.FILES['image']
                        products.save()
                        data = {'error':'3','data':'Product Updated'}
                    else:
                        data = {'error':'4','data':'Please Add All details for Product'}
                else:
                    data = {'error':'6','data':'This product is not available'}
            else:
                data = {'error':'5','data':'Please Enter Product ID to update it'}
        else:
            data = {'error':'1','products' : 'Unauthorised User'}
    else:
        data = {'error':'2','data':'Please use email and password to update products'}
    return Response(data)

@api_view(['POST'])
def delete_products(request):
    data = {}
    if 'email' in request.POST and 'password' in request.POST and request.POST['email'] and request.POST['password']:
        if user.objects.filter(email=request.POST['email'],password=request.POST['password']).exists():
            if 'pk' in request.POST:
                if product.objects.filter(id=request.POST['pk']).exists():
                    if 'pk' in request.POST:
                        products = product.objects.get(id=request.POST['pk'])
                        products.delete()
                        data = {'error':'3','data':'Product Deleted'}
                    else:
                        data = {'error':'4','data':'Please Add Product id'}
                else:
                    data = {'error':'6','data':'This product is not available'}
            else:
                data = {'error':'5','data':'Please Enter Product ID to Delete it'}
        else:
            data = {'error':'1','products' : 'Unauthorised User'}
    else:
        data = {'error':'2','data':'Please use email and password to delete products'}
    return Response(data)