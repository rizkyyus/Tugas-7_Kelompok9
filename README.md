# Tugas-7_Kelompok9

# Django Katalog Produk Sederhana

Proyek ini adalah implementasi sederhana website katalog produk menggunakan framework Django. Website ini memiliki 5 halaman utama dengan masing-masing URL tersendiri dan menggunakan Function-Based Views.

## Fitur

- **Homepage** (`/`): Menampilkan halaman utama dengan produk unggulan.
- **Halaman Daftar Produk** (`/produk/`): Menampilkan semua produk yang tersedia.
- **Halaman Detail Produk** (`/produk/1/`): Menampilkan informasi detail suatu produk.
- **Halaman Kontak** (`/kontak/`): Menampilkan informasi kontak dan form pesan.
- **Halaman Tentang Kami** (`/about/`): Menampilkan informasi tentang toko online.

## Teknologi yang Digunakan

- Python 3.7+
- Django 4.0+
- HTML
- CSS (inline styling)

## Struktur Proyek

```
toko/
├── manage.py                          # Script untuk mengelola proyek Django
├── toko/                              # Folder konfigurasi proyek
│   ├── __init__.py                    # File inisialisasi Python
│   ├── settings.py                    # Konfigurasi proyek (database, apps, middleware, dll.)
│   ├── urls.py                        # URL router utama proyek
│   ├── asgi.py                        # Konfigurasi ASGI untuk deployment
│   └── wsgi.py                        # Konfigurasi WSGI untuk deployment
└── produk/                            # Aplikasi 'produk'
    ├── __init__.py                    # File inisialisasi Python
    ├── admin.py                       # Konfigurasi admin panel
    ├── apps.py                        # Konfigurasi aplikasi Django
    ├── models.py                      # Model database
    ├── tests.py                       # Unit test
    ├── views.py                       # Function-Based Views untuk menangani permintaan HTTP
    ├── urls.py                        # URL router aplikasi 'produk'
    ├── migrations/                    # Folder migrasi database
    └── templates/                     # Folder template HTML
        └── produk/                    # Sub-folder aplikasi 'produk'
            ├── index.html             # Template homepage
            ├── produk_list.html       # Template daftar produk
            ├── produk_detail.html     # Template detail produk
            ├── kontak.html            # Template halaman kontak
            └── about.html             # Template halaman tentang kami
```

## Instalasi dan Menjalankan Proyek

### Prasyarat

- Python 3.7 atau yang lebih baru
- pip (Python package installer)

### Langkah-langkah Instalasi

1. Clone repository ini:
   ```bash
   git clone https://github.com/username/django-katalog-produk.git
   cd django-katalog-produk
   ```

2. Buat virtual environment (opsional tapi direkomendasikan):
   ```bash
   python -m venv env
   ```

3. Aktifkan virtual environment:
   - Windows:
     ```bash
     env\Scripts\activate
     ```
   - Mac/Linux:
     ```bash
     source env/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install django
   ```

5. Jalankan migrasi database:
   ```bash
   python manage.py migrate
   ```

6. Jalankan server development:
   ```bash
   python manage.py runserver
   ```

7. Buka browser dan akses:
   ```
   http://127.0.0.1:8000/
   ```


## Pengembangan Lebih Lanjut

Beberapa ide untuk mengembangkan proyek ini lebih lanjut:

1. Implementasi database dengan Django Models
2. Sistem autentikasi pengguna
3. Keranjang belanja dan fitur checkout
4. Integrasi pembayaran
5. Pencarian dan filter produk
6. Optimasi SEO
7. Responsive design



## Pembuat

- Rizky Yusmansyah   (2208107010024)
- Fadli Ahmad Yazid  (2208107010032)
- Andika Pebriansyah (2208107010058)
