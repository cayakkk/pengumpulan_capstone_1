from tabulate import tabulate

#Collection Data
data_mobil = {
    'A 1145 LE': {'Merk': 'Daihatsu', 'Tipe': 'Ayla', 'Transmisi': 'MT', 'Seats': 4, 'Harga': 280000},
    'A 1623 EFG': {'Merk': 'Toyota', 'Tipe': 'Avanza', 'Transmisi': 'MT', 'Seats': 6, 'Harga': 370000},
    'B 231 AF': {'Merk':'Mitsubishi', 'Tipe': 'Expander', 'Transmisi':'AT', 'Seats': 6, 'Harga': 430000}
}

#Fungsi untuk memeriksa validitas plat nomor
def is_valid_plate(plate):
    parts = plate.split()
    if len(parts) == 3 and parts[0].isalpha() and parts[1].isdigit() and parts[2].isalpha():
        if 1 <= len(parts[0]) <= 2 and 1 <= len(parts[1]) <= 4 and 1 <= len(parts[2]) <= 3:
            return True
    return False

#Print tabel data mobil
def cetak_data_mobil():
    stok_mobil = []
    for key, value in data_mobil.items():
        value['Plat'] = key  #Menambahkan key: plat, value: key data_mobil ke dalam dictionary value
        stok_mobil.append(value)
    print(tabulate(stok_mobil, headers="keys", tablefmt="double_grid", stralign="center", numalign="center"))

#Filter Mobil
def filter_car_by_primary_key(data_mobil): 
    if len(data_mobil) == 0:
        print('Tidak ada data tersimpan.')
    else:
        plat = input('Masukkan plat mobil yang ingin dicari: ')
        if is_valid_plate(plat):
            if plat in data_mobil.keys():
                hasil_pencarian = []
                mobil = data_mobil[plat]
                hasil_pencarian.append(mobil)
                print(tabulate(hasil_pencarian, headers="keys", tablefmt="double_grid", stralign="center", numalign="center"))
            else:
                print(f"Tidak ada mobil dengan plat {plat}")
        else:
            print('Nomor plat tidak valid. \nContoh format yang benar: B 1234 XYZ')

def filter_car_by_category(data_mobil): 
    if len(data_mobil) == 0:
        print('Tidak ada data tersimpan.')
    else:
        print('\tPilih Mobil Berdasarkan Spesifikasi')
        print('Masukkan salah satu atau lebih spesifikasi berikut (Biarkan kosong jika tidak ingin mengisi):')
        merk = input('Masukkan merk mobil: ').strip()
        tipe = input('Masukkan tipe mobil: ').strip()
        transmisi = input('Masukkan transmisi mobil (AT/MT): ').strip()
        seats = input('Masukkan jumlah seats mobil: ').strip()
        harga = input('Masukkan harga rental mobil: ').strip()
    
        #Filter mobil berdasarkan input yang diberikan
        hasil_pencarian = []
        for plat, mobil in data_mobil.items():
            kesesuaian = True
            if merk and merk.lower() != mobil['Merk'].lower():
                kesesuaian = False
            if tipe and tipe.lower() != mobil['Tipe'].lower():
                kesesuaian = False
            if transmisi and transmisi.lower() != mobil['Transmisi'].lower():
                kesesuaian = False
            if seats and seats != mobil['Seats']:
                kesesuaian = False
            if harga and harga != mobil['Harga']:
                kesesuaian = False
            
            #Jika semua spesifikasi cocok, tambahkan mobil ke hasil pencarian
            if kesesuaian:
                mobil['Plat'] = plat  #Menambahkan plat mobil ke data mobil
                hasil_pencarian.append(mobil)

        #Tampilkan hasil pencarian atau pesan jika tidak ada yang cocok
        if len(hasil_pencarian) > 0:
            print(tabulate(hasil_pencarian, headers="keys", tablefmt="double_grid", stralign="center", numalign="center"))
        else:
            print("Tidak ada mobil yang sesuai dengan kriteria yang diberikan.")


#Menampilkan Daftar Mobil
def sub1_read_data(): 
    while True:
        print('''
            Menu Tampilan Data Mobil:
            1 : Tampilkan seluruh data mobil
            2 : Filter Data Berdasarkan Primary Key 
            3 : Filter Data Berdasarkan Kriteria
            4 : Kembali ke Menu Utama
            ''')
        opsi_sub1 = input('Masukkan angka sesuai menu yang ingin dipilih: ')
        if opsi_sub1 == '1':
            cetak_data_mobil()
        elif opsi_sub1 == '2':
            filter_car_by_primary_key(data_mobil)
        elif opsi_sub1 == '3':
            filter_car_by_category(data_mobil)
        elif opsi_sub1 == '4':
            break
        else:
            print('Masukkan angka sesuai menu yang tersedia.')


#Menambah Data ke Daftar Mobil
def sub2_add_data():
    while True:
        print('''
        Menu Menambah Data Mobil
        1 : Menambah Data Mobil
        2 : Keluar
            ''')
        opsi_sub2 = input('Pilih menu berdasarkan angka yang tertera: ')
        if opsi_sub2 == '1':
            print('\t Menambah Data Mobil')
            while True:
                plat_baru = input('Masukkan Nomor Plat: ').strip().upper()
                if is_valid_plate(plat_baru):
                    if plat_baru in data_mobil:
                        print('Data sudah ada.')
                    else:
                        merk_baru = input('Masukkan merk mobil: ').capitalize()
                        tipe_baru = input('Masukkan tipe mobil: ').capitalize()
                        
                        #Validasi transmisi
                        while True:
                            trans_baru = input('Masukkan transmisi mobil (AT/MT): ').strip().upper()
                            if trans_baru in ['AT', 'MT']:
                                break
                            else:
                                print("Transmisi tidak valid. Masukkan hanya 'AT' atau 'MT'.")
                        
                        #Validasi seats
                        while True:
                            try:
                                seats_baru = int(input('Masukkan jumlah seats mobil: '))
                                if seats_baru > 1 and seats_baru < 9:
                                    break
                                else:
                                    print("Jumlah seats harus lebih dari 1.")
                            except ValueError:
                                print("Seats harus berupa angka.")
                        
                        #Validasi harga
                        while True:
                            try:
                                harga_baru = int(input('Masukkan harga rental mobil/hari: Rp '))
                                if harga_baru > 100000 and harga_baru <1000000 and harga_baru % 1000 == 0:
                                    break
                                else:
                                    print("Harga harus dalam rentang Rp 150000 dan Rp1000000.")
                            except ValueError:
                                print("Harga harus berupa angka.")

                        #Membuat dictionary baru dengan plat_baru sebagai kunci
                        mobil_baru = {
                            'Merk': merk_baru,
                            'Tipe': tipe_baru,
                            'Transmisi': trans_baru,
                            'Seats': seats_baru,
                            'Plat': plat_baru,
                            'Harga': harga_baru
                        }

                        print("Data mobil baru:")
                        print(tabulate([mobil_baru], headers="keys", tablefmt="double_grid", stralign="center", numalign="center"))
                        
                        while True:
                            checker_1 = input('Apakah anda yakin ingin menambahkan data mobil di atas? (ya/tidak): ').strip().lower()
                            if checker_1 == 'ya':
                                data_mobil[plat_baru] = mobil_baru
                                print('Data mobil berhasil ditambahkan.')
                                break
                            elif checker_1 == 'tidak':
                                print('Data mobil tidak ditambahkan.')
                                break
                            else:
                                print('Masukkan input yang sesuai YA atau TIDAK.')
                    break
                else:
                    print('Nomor plat tidak valid. \nContoh format yang benar: B 1234 XYZ')
        elif opsi_sub2 == '2':
            break
        else:
            print('Masukkan input yang sesuai')

def sub3_update_data():
    while True:
        print('''
        Menu Update Data Mobil
        1: Update Data Mobil
        2: Cari Data Mobil
        3: Keluar
            ''')
        opsi_sub3 = input('Pilih menu berdasarkan angka yang tertera: ')
        if opsi_sub3 == '1':
            while True:
                index_mobil = input('Masukkan nomor plat mobil yang ingin diubah: ').strip().upper()
                if is_valid_plate(index_mobil):
                    if index_mobil in data_mobil:
                        print(tabulate([data_mobil[index_mobil]], headers="keys", tablefmt="double_grid", stralign="center", numalign="center"))
                        checker_3 = input('Apakah anda yakin ingin mengubah data mobil tersebut? (YA/TIDAK): ').lower()
                        if checker_3 == 'ya':
                            updated_data = data_mobil[index_mobil].copy()  # Salin data ke variabel sementara
                            print(f'''\t Update Data Mobil {index_mobil}
                            1. Merk
                            2. Tipe
                            3. Transmisi
                            4. Jumlah Seats
                            5. Harga Rental
                            ''')
                            opsi_update = input('Masukkan opsi yang ingin diubah: ')
                            if opsi_update == '1':
                                updated_data["Merk"] = input('Masukkan Merk Mobil Terbaru: ')
                            elif opsi_update == '2':
                                updated_data["Tipe"] = input('Masukkan Tipe Mobil Terbaru: ')
                            elif opsi_update == '3':
                                updated_data["Transmisi"] = input('Masukkan Jenis Transmisi Terbaru: ')
                            elif opsi_update == '4':
                                while True:
                                    try:
                                        seats_baru = int(input('Masukkan Jumlah Seats Terbaru: '))
                                        if seats_baru > 0 and seats_baru < 9:
                                            updated_data["Seats"] = seats_baru
                                            break
                                        else:
                                            print("Jumlah seats harus lebih dari 0 dan kurang dari 9.")
                                    except ValueError:
                                        print("Seats harus berupa angka.")
                            elif opsi_update == '5':
                                while True:
                                    try:
                                        harga_baru = int(input('Masukkan harga rental mobil/hari: Rp '))
                                        if harga_baru > 150000 and harga_baru < 1000000 and harga_baru % 1000 == 0:
                                            break
                                        else:
                                            print("Harga harus lebih dari Rp 100000.")
                                    except ValueError:
                                        print("Harga harus berupa angka.")
                            
                            print(tabulate([updated_data], headers="keys", tablefmt="double_grid", stralign="center", numalign="center"))
                            checker_4 = input('Apakah Anda yakin ingin memperbaharui data mobil sebagai data di atas? (YA/TIDAK): ').lower()
                            if checker_4 == 'ya':
                                data_mobil[index_mobil] = updated_data  # Simpan perubahan ke data asli
                                print('Data berhasil disimpan.')
                                break
                            elif checker_4 == 'tidak':
                                print('Data tidak disimpan.')
                                break
                            else:
                                print('Masukkan input yang sesuai.')
                        elif checker_3 == 'tidak':
                            break
                        else:
                            print('Masukkan input yang sesuai.')
                    else:
                        print('Nomor plat tidak ditemukan.')
                else:
                    print('Nomor plat tidak sesuai format. Contoh yang benar: B 1234 XYZ')
        elif opsi_sub3 == '2':
            cari_mobil(data_mobil)
        elif opsi_sub3 == '3':
            break
        else:
            print('Masukkan input yang sesuai.')


def sub4_delete_data():
    while True:
        print('''
        Menu Hapus Data Mobil
        1 : Hapus Data Mobil
        2 : Keluar
        ''')
        opsi_sub4 = input('Pilih menu berdasarkan angka yang tertera: ')
        if opsi_sub4 == '1':
            while True:
                hapus_mobil = input('Masukkan nomor plat mobil yang ingin dihapus: ')
                if is_valid_plate(hapus_mobil):
                    if hapus_mobil in data_mobil:
                        print("Data mobil yang akan dihapus:")
                        print(tabulate([data_mobil[hapus_mobil]], headers="keys", tablefmt="double_grid", stralign="center", numalign="center"))
                        checker2 = input('Apakah Anda yakin ingin menghapus data mobil ini? (ya/tidak): ')
                        if checker2.lower() == 'ya':
                            del data_mobil[hapus_mobil]
                            print(f'Data mobil dengan nomor plat {hapus_mobil} telah dihapus.')
                            break
                        elif checker2.lower() == 'tidak':
                            print('Penghapusan dibatalkan.')
                            break
                        else:
                            print('Masukkan inputan yang sesuai.')
                    else:
                        print(f'Data mobil dengan plat {hapus_mobil} tidak ada.')
                        break
                else:
                    print('Nomor plat tidak valid. \nContoh format yang benar: B 1234 XYZ')
        elif opsi_sub4 == '2':
            break
        else:
            print('Masukkan input yang sesuai')


def menu_utama ():
    while True:
        print('''
        Selamat Datang di Future Rental
        Menu Utama
        1 : Menampilkan Data Mobil
        2 : Menambahkan Data Mobil
        3 : Memperbaharui Data Mobil
        4 : Menghapus Data Mobil
        5 : Keluar
            ''')
        opsi_submenu = input('Pilih menu berdasarkan angka yang tertera: ')
        if opsi_submenu == '1':
            sub1_read_data()
        elif opsi_submenu =='2':
            sub2_add_data()
        elif opsi_submenu == '3':
            sub3_update_data()
        elif opsi_submenu == '4':
            sub4_delete_data()
        elif opsi_submenu == '5':
            print('Program berhenti.')
            break
        else:
            print('Masukkan angka sesuai menu yang tersedia.')
menu_utama()
