from django.shortcuts import render
from django.views import View

# Create your views here.

class CartView(View):
    def get(self,request):
        return render(request,'orders/cart.html')

class CartAddView(View):

    def get(self,request,product_id):
        pass
