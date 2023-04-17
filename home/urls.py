from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product_detail'),
    path('bucket/', views.BucketHome.as_view(), name='bucket'),
    path('delete_obj_bucket/<key>', views.DeleteBucketObject.as_view(), name='delete_obj_bucket'),
    path('download_obj_bucket/<key>', views.DownloadBucketObject.as_view(), name='download_obj_bucket'),

]
