from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from orders.forms import CartAddForm
from utils import IsAdminUserMixin
from . import tasks
from .models import Product, Category




class HomeView(View):



    def get(self, request, category_slug=None):

        products = Product.objects.filter(available=True)
        categories = Category.objects.filter(is_sub=False)
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'home/home.html', {'products': products, 'categories': categories})


class ProductDetailView(View):

    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        form = CartAddForm()
        return render(request, 'home/product_detail.html', {'product': product, 'form': form})


class BucketHome(IsAdminUserMixin, View):
    template_name = 'home/bucket.html'

    def get(self, request):


        objects = tasks.all_bucket_object_task()
        return render(request, self.template_name, {'objects': objects})


class DeleteBucketObject(IsAdminUserMixin, View):
    def get(self, request, key):
        tasks.delete_object_bucket(key)
        messages.success(request, 'your object will be deleted soon', 'info')
        return redirect('home:bucket')


class DownloadBucketObject(IsAdminUserMixin, View):

    def get(self, request, key):
        tasks.download_bucket_object(key)
        messages.success(request, 'download will start soon', 'info')
        return redirect('home:bucket')

