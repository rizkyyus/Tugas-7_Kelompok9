# produk/views.py
from django.shortcuts import render
from django.http import HttpResponse

# Data dummy untuk produk
produk_data = [
    {
        'id': 1,
        'nama': 'Laptop ASUS',
        'harga': 'Rp 15.000.000',
        'deskripsi': 'Laptop gaming dengan spesifikasi tinggi'
    },
    {
        'id': 2,
        'nama': 'Smartphone Samsung',
        'harga': 'Rp 8.000.000',
        'deskripsi': 'Smartphone dengan kamera terbaik di kelasnya'
    },
    {
        'id': 3,
        'nama': 'Headphone Sony',
        'harga': 'Rp 2.500.000',
        'deskripsi': 'Headphone dengan noise cancelling'
    },
    {
        'id': 4,
        'nama': 'Smart TV LG',
        'harga': 'Rp 10.000.000',
        'deskripsi': 'Smart TV 55 inch dengan resolusi 4K'
    },
    {
        'id': 5,
        'nama': 'Tablet Apple',
        'harga': 'Rp 12.000.000',
        'deskripsi': 'Tablet dengan performa tinggi untuk desain dan kreativitas'
    }
]

def index(request):
    """View untuk homepage"""
    return render(request, 'produk/index.html')

def produk_list(request):
    """View untuk menampilkan daftar produk"""
    context = {
        'produk_list': produk_data
    }
    return render(request, 'produk/produk_list.html', context)

def produk_detail(request, id):
    """View untuk menampilkan detail produk berdasarkan ID"""
    # Cari produk berdasarkan ID
    produk = None
    for item in produk_data:
        if item['id'] == id:
            produk = item
            break
    
    # Jika produk ditemukan
    if produk:
        context = {
            'produk': produk
        }
        return render(request, 'produk/produk_detail.html', context)
    else:
        return HttpResponse("Produk tidak ditemukan", status=404)

def kontak(request):
    """View untuk halaman kontak"""
    return render(request, 'produk/kontak.html')

def about(request):
    """View untuk halaman tentang kami"""
    return render(request, 'produk/about.html')