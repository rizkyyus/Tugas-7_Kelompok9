# produk/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Homepage
    path('produk/', views.produk_list, name='produk_list'),  # Halaman daftar produk
    path('produk/<int:id>/', views.produk_detail, name='produk_detail'),  # Halaman detail produk
    path('kontak/', views.kontak, name='kontak'),  # Halaman kontak
    path('about/', views.about, name='about'),  # Halaman tentang kami (halaman ke-5)
]