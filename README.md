## Capstone Module 1 | Derielle Aisyah Ahmad JCDS2602

## Program Manajemen Toko Pupuk Horizon
### Deskripsi
Program Manajemen Toko Pupuk Horizon merupakan sistem manajemen sederhana untuk toko pupuk. Program manajemen ini memungkinkan pengguna untuk melihat daftar produk, membeli produk dan mengelola stok produk melalui menu administrator. Data produk dalam program ini ditampilkan dengan format tabel menggunakan pustaka `tabulate`

### Fitur
Program manajemen ini merupakan program CRUD. Fitur yang terdapat pada program manajemen, sebagai berikut:
1. Menampilkan Daftar Produk
    - Menampilkan seluruh produk beserta stok, harga, dan produsen
    - Menampilkan produk berdasarkan produsen tertentu
2. Membeli Produk
    - Pengguna dapat memilih dan membeli produk
    - Menampilkan keranjang belanja dan total harga serta melakukan pembayaran
    - Mengelola stok produk setelah pembelian
3. Menu Administrator *(Dilindungi dengan Password)*
    - Menambahkan produk baru
    - Menambahkan stok produk yang sudah ada
    - Menghapus produk berdasarkan indeks produk atau seluruh daftar produk
4. Opsi Keluar dari Program

### Ketentuan Program
- Phython 3.x
- Pustaka `tabulate` (Jika belum terinstall, gunakan `pip install tabulate`)

### Cara Menggunakan Program
1. Jalankan program Python.
2. Pilih menu utama:
     1. Menampilkan daftar produk.
     2. Membeli produk.
     3. Menu administrator
     4. Keluar dari program.
3. Ikuti instruksi di layar untuk melakukan tindakan yang diinginkan.

### Catatan
- Program akan terus berjalan hingga pengguna memilih opsi keluar
- Menu administrator hanya bisa diakses dengan password `272`
- Jika stok produk habis, maka produk tidak dapat dibeli

### Lisensi
Program ini dapat digunakan dan dimodifikasi secara bebas
