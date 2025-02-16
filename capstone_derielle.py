import os
import platform

def clear_terminal():

    system = platform.system().lower()

    if system == 'windows':
        os.system('cls')

    else:
        os.system('clear')

clear_terminal()

# CAPSTONE MODUL 1
# TOKO PUPUK

from tabulate import tabulate
headers = ['Index','Nama Produk','Stok','Harga','Produsen']

PRODUKdict =    { 
        'Nama Produk' : ['PUPUK NPK MUTIARA', 'PUPUK PHONSKA', 'PUPUK DAUN GANDASIL', 'PUPUK ZA', 'PUPUK UREA'],
        'Stock' : [10, 13, 20, 15, 8],
        'Harga' :[18000, 12000, 25000, 10000, 10000],
        'Produsen': ['MEROKE', 'PUPUK INDONESIA','GANDASIL', 'PETROKIMIA', 'PUPUK INDONESIA']
                }

cart = []

# Menampilkan DAFTAR PRODUK 
def produk():
    while True:
        print()
        print('MENU PRODUK')
        print('1. Tampilkan data seluruh produk \n2. Tampilkan data produk berdasarkan produsen \n3. Kembali ke MENU UTAMA')
        try:
            menuproduk = int(input('Masukkan angka menu yang ingin ditampilkan: '))
            if menuproduk == 1:
                print('\nDAFTAR PRODUK')
                print(tabulate(PRODUKdict, headers=headers, showindex='always'))
                # kembali ke menu produk
            elif menuproduk == 2:
                while True:
                    try: 
                        namaprodusen = input('Masukkan PRODUSEN PRODUK yang ingin ditampilkan: ').upper()
                        mencariprodusen = [
                                            [PRODUKdict['Nama Produk'][i], 
                                             PRODUKdict['Stock'][i], 
                                             PRODUKdict['Harga'][i], 
                                             PRODUKdict['Produsen'][i]]
                        for i in range(len(PRODUKdict['Produsen']))
                        if namaprodusen in PRODUKdict['Produsen'][i].upper()  # Pencarian berdasarkan nama PRODUSEN
                                            ]
                        if mencariprodusen:
                            print(tabulate(mencariprodusen, headers=["Nama Produk", "Stock", "Harga", "Produsen"], showindex='always'))
                            break
                        else:
                            print("Produsen tidak ditemukan")     
                    except:
                        print('Produk tidak ada, silahkan input nama produk dengan benar')
            elif menuproduk == 3:
                break
            else:
                print('Input menu tidak valid')
                continue # Kembali ke MENU PRODUK
        except:
            print('Input menu tidak valid')

# UPDATE >> Membeli Produk
def beliproduk(): 
    global PRODUKdict
    global cart
    while True:
        print('\nDAFTAR PRODUK')
        print(tabulate(PRODUKdict, headers=headers, showindex='always'))
        try:
            index_beli = int(input('Masukkan index produk yang ingin dibeli: '))
            if index_beli >= len(PRODUKdict['Nama Produk']): # KALAU INDEX YG DIMASUKKAN OUT OF RANGE
                print('Input tidak valid')
                continue
        except ValueError: # KALAU INDEX YG DIMASUKKAN BUKAN INT
            print('Input tidak valid')
            continue 
        produkBELI = PRODUKdict['Nama Produk'][index_beli]
        try:
            jumlahBELI = int(input('Masukkan jumlah produk yang ingin dibeli: '))
            if jumlahBELI == ValueError:
                print('Input tidak valid')
        except:
            continue
        stock = PRODUKdict['Stock'][index_beli]
        print()
        if jumlahBELI > stock:
            print(f'Stok produk tidak cukup, stok {produkBELI} saat ini tersisa {stock}')
        elif jumlahBELI <= stock:
            cart.append({'Index': index_beli,
                            'Nama Produk' : produkBELI, 
                            'Stock': jumlahBELI, 
                            'Harga': PRODUKdict['Harga'][index_beli],
                            'Produsen': PRODUKdict['Produsen'][index_beli]
                            })
            print('\n Isi Cart: ')
            print(tabulate(cart, headers='keys'))
            print()
        beliagain = input('Apakah mau membeli produk lain? ya/tidak :').lower()
        if beliagain == 'ya':
            PRODUKdict['Stock'][index_beli] -= jumlahBELI
            continue
        elif beliagain =='tidak':
            PRODUKdict['Stock'][index_beli] -= jumlahBELI
            break
        else: # KALAU INPUT YG DIMASUKAN BUKAN ya/tidak
            print('Input tidak valid')
            cart.clear()
            continue # Kembali ke DAFTAR PRODUK 
    if cart:
        total_harga = 0
        print('\nDaftar Belanja')
        print(tabulate(cart, headers='keys'))
        for item in cart:
            total_item = item['Stock']*item['Harga']
            total_harga += total_item
        print(f'Total harga yang harus dibayarkan: {total_harga}')
    while True:
        uang = int(input('Masukkan jumlah uang: '))
        if uang < total_harga:
            print(f'Transaksi anda dibatalkan uangnya kurang sebesar {total_harga-uang}')
        elif uang == total_harga:
            print('Terima kasih telah berbelanja')
            for item in cart:
                PRODUKdict['Stock'][item['Index']] -= item['Stock']
            break
        elif uang > total_harga:
            print(f'Terima kasih \n Uang kembali anda: {uang-total_harga}')
            break
    cart.clear()

def DELETEPROD():
    while True:
        print('\nHAPUS PRODUK')
        print('1. Hapus produk berdasarkan index produk \n2. Hapus daftar seluruh produk \n3. Kembali ke MENU ADMINISTRATOR')
        try:
            pilihanhapus = int(input('Masukkan ANGKA menu yang diinginkan:'))

            #HAPUS BERDASARKAN INDEX PRODUK
            if pilihanhapus == 1: # 
                while True:
                    print('\nDAFTAR PRODUK')
                    print(tabulate(PRODUKdict, headers=headers, showindex='always'))
                    try:
                        produkdel = int(input('Masukkan index produk yang ingin dihapus: '))
                        if 0 <= produkdel < len(PRODUKdict['Nama Produk']):
                            print()
                            print(f'Apakah anda yakin untuk menghapus produk {PRODUKdict['Nama Produk'][produkdel]}')
                            print('1. Ya \n2. Tidak ')
                            try:
                                hapus = int(input('Masukkan ANGKA pilihan: '))
                                if hapus == 1: # YA, YAKIN HAPUS
                                    if 0 <= produkdel < len(PRODUKdict['Nama Produk']): 
                                        del PRODUKdict['Nama Produk'][produkdel]
                                        del PRODUKdict['Stock'][produkdel]
                                        del PRODUKdict['Harga'][produkdel]
                                        del PRODUKdict['Produsen'][produkdel]
                                        print('Produk telah berhasil dihapus')
                                        print(tabulate(PRODUKdict, headers='keys',showindex='always'))
                                        print('Daftar produk telah diperbarui') 
                                        break # Kembali ke  MENU HAPUS
                                elif hapus == 2: # TIDAK JADI HAPUS
                                    print(f'Produk {PRODUKdict['Nama Produk'][produkdel]} batal dihapus')
                                    break # Kembali ke MENU HAPUS
                                else: # jika input bukan 1/2
                                    print('ELSEInput tidak valid')
                                    continue # Kembali ke masukkan index produk yg dihapus
                            except: # jika input str
                                print('Input tidak valid')
                                continue # Kembali ke masukkan index produk yg dihapus
                        else: 
                            print('Tidak ada produk dengan index tersebut') # Ketika index produk yg dimasukkan out of range
                            continue
                    except:
                        print('Tidak ada produk dengan index tersebut')
                        print('Masukkan index produk yang valid')
                        continue # Kembali ke masukkan index produk yg dihapus

            #HAPUS SELURUH PRODUK
            elif pilihanhapus == 2:
                print()
                print('Apakah anda yakin untuk menghapus seluruh produk? ')
                print('1. Ya \n2. Tidak')
                try:
                    hapusSEMUA = int(input('Masukkan ANGKA pilihan: '))
                    if hapusSEMUA == 1: # YA HAPUS SEMUA
                        print('\nHAPUS SELURUH PRODUK')
                        print('\nSilahkan masukkan password administrator untuk menghapus seluruh produk: ')
                        password = '272'
                        pw = input('Masukkan Password Administrator: ')
                        if pw == password:
                            PRODUKdict.clear()
                            print('Seluruh produk telah dihapus')
                            print()
                            print(tabulate(PRODUKdict, headers=headers,showindex='always'))
                        else:
                            print('Password salah, kembali ke MENU HAPUS')
                            continue # Kembali ke MENU HAPUS
                    if hapusSEMUA == 2: # TIDAK JADI HAPUS SEMUA
                        print('Hapus seluruh produk dibatalkan')
                        continue # Kembali ke MENU HAPUS
                except:
                    print('Input tidak valid')
                    continue # Kembali ke MENU HAPUS

            # Kembali ke MENU ADMINISTRATOR    
            elif pilihanhapus == 3:
                break
            else:
                print('Input tidak valid')
        except:
            continue        

# PASSWORD ADMINISTRATOR
def PASS():
    print('MENU ADMINISTRATOR')
    password = '272'
    while True:
        pw = (input('Masukkan Password Administrator: '))
        if pw == password:
            print('Password Benar')
            return True
        else:
            print('Password Salah \nMasukkan Password Kembali')
            PASS() #KEMBALI KE PASS

# MENU ADMINISTRATOR
def ADMIN():
    while True:
        print()
        print('MENU ADMINISTRATOR')
        print('1. Menambah Produk Baru \n2. Menambah Stok Produk \n3. Menghapus Produk \n4. Kembali ke Menu Utama')
        try:
            menuADmin = int(input('Masukkan angka menu yang diinginkan: '))
        except ValueError:
            print('Input tidak valid')
            continue # Kembali ke MENU ADMINISTRATOR

        # Kembali ke MENU UTAMA      
        if menuADmin == 4: 
            break

        # Menginput produk baru
        elif menuADmin == 1: 
            print('\nDAFTAR PRODUK')
            print(tabulate(PRODUKdict, headers=headers, showindex='always'))
            print('INPUT PRODUK BARU')
            nprodukbaru = input('Masukkan nama produk baru: ').upper()
            try:
               stockbaru = int(input('Masukkan jumlah stok produk baru: ')) 
            except ValueError:
                print('Input tidak valid')
                continue # Kembali ke MENU ADMINISTRATOR
            hargabaru = int(input('Masukkan harga produk baru: '))
            produsenbaru = input('Masukan produsen produk baru: ').upper()
            print('Tambah produk ke DAFTAR PRODUK? \n1. Ya \n2. Tidak')
            while True:
                print()
                try:
                    tambahprodukyn = int(input('Masukkan ANGKA pilihan: '))
                    if tambahprodukyn == 1:
                        PRODUKdict['Nama Produk'].append(nprodukbaru)
                        PRODUKdict['Stock'].append(stockbaru)
                        PRODUKdict['Harga'].append(hargabaru)
                        PRODUKdict['Produsen'].append(produsenbaru)
                        print()
                        print('DAFTAR PRODUK')
                        print(tabulate(PRODUKdict, headers='keys',showindex='always'))
                        print('Produk telah ditambahkan')
                        break # Kembali ke MENU ADMINISTRATOR
                    elif tambahprodukyn == 2:
                        break # Kembali ke MENU ADMINISTRATOR
                    else:
                        print()
                        print('Input tidak valid')
                        continue
                except:
                    print('Input tidak valid')
                    continue
                   
        # Menambah Stock Produk #UPDATE
        elif menuADmin == 2: 
            print('\nDAFTAR PRODUK')
            print(tabulate(PRODUKdict, headers=headers, showindex='always'))
            print('TAMBAH STOCK PRODUK')
            while True:
                try: 
                    namaproduk = input('Masukkan NAMA PRODUK yang akan ditambah stok: ').upper()
                    if namaproduk in PRODUKdict['Nama Produk']:
                        try:
                            stocktambah = int(input('Masukkan jumlah stock produk yang akan ditambahkan: '))
                        except ValueError:
                            print('Input tidak valid')
                            continue
                        indexTambahStok = PRODUKdict['Nama Produk'].index(namaproduk)
                        PRODUKdict['Stock'][indexTambahStok] += stocktambah
                        print('\nDAFTAR PRODUK')
                        print(tabulate(PRODUKdict, headers=headers, showindex='always'))
                        print(f'Stok {namaproduk} telah ditambah')
                        break #KEMBALI KE MENU ADMINISTATOR
                    else:
                        print('Produk tidak ada, silahkan input nama produk dengan benar')
                        continue
                except:
                    print('Produk tidak ada, silahkan input nama produk dengan benar')

        # Menghapus Produk #DELETE
        elif menuADmin == 3:
            DELETEPROD()  
        else:
            print('Index tidak valid')
            break # Kembali ke MENU UTAMA 

#EXIT PROGRAM
def EXIT():
    print('Terima Kasih')
    
# MENU UTAMA
while True:
    print('\nSelamat Datang di TOKO PUPUK HORIZON')
    print('List Menu')
    print('1. Menampilkan Daftar Produk \n2. Membeli Produk \n3. Menu Administrator \n4. Exit Program')
    try:
        menu = int(input('Masukkan angka menu yang diinginkan: '))
    except ValueError:
        print('Input tidak valid')
        continue
    if menu == 1:
        produk()
    elif menu == 2:
        beliproduk()
    elif menu == 3:
        PASS()
        ADMIN()
    elif menu == 4:
        EXIT()
        break
    else:
        print('Pilihan menu tidak valid')
        continue



