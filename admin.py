def tambah_barang(nama, harga, jumlah):
    with open ("storage/barang.txt", "a", encoding="utf-8") as file:
        file.write(f"{nama}|{harga}|{jumlah}\n")

def cek_barang():
    
    with open("storage/barang.txt", "r", encoding="utf-8") as file:
            daftar_barang = file.readlines()

    print("\n=== Daftar Barang ===")

    if not daftar_barang:
        print("Belum ada barang.")
    else:
        for barang in daftar_barang:
            nama, harga, jumlah = barang.strip().split("|")
            print(f"""
Nama   : {nama}
Harga  : {harga}
Jumlah : {jumlah}
=================""")
    
    while True:
        kembali = input(
            "\nKembali ke menu sebelumnya? (y): "
        ).lower()

        if kembali == "y":
            break
        else:
            print("Pilihan tidak valid. Masukkan y.")

def update_barang(nama_barang, harga_baru, jumlah_baru):
        daftar_barang = []

        with open("storage/barang.txt", "r", encoding="utf-8") as file:
            for barang in file:
                nama, harga, jumlah = barang.strip().split("|")
                daftar_barang.append([nama, harga, jumlah])

        ditemukan = False

        for barang in daftar_barang:
            if barang[0].lower() == nama_barang.lower():
                if harga_baru is not None:
                    barang[1] = str(harga_baru)
                if jumlah_baru is not None:
                    barang[2] = str(jumlah_baru)
                ditemukan = True
                break

        if not ditemukan:
            print("Barang tidak ditemukan.\n")
            return False

        with open("storage/barang.txt", "w", encoding="utf-8") as file:
            for barang in daftar_barang:
                file.write(f"{barang[0]}|{barang[1]}|{barang[2]}\n")
            return True
                
def hapus_barang(nama_barang):
    daftar_barang = []

    with open("storage/barang.txt", "r", encoding="utf-8") as file:
        for barang in file:
            nama, harga, jumlah = barang.strip().split("|")
            daftar_barang.append([nama, harga, jumlah])

    ditemukan = False

    for i, barang in enumerate(daftar_barang):
        if barang[0].lower() == nama_barang.lower():
            del daftar_barang[i]
            ditemukan = True
            break

    if not ditemukan:
        print("Barang tidak ditemukan.\n")
        return False

    with open("storage/barang.txt", "w", encoding="utf-8") as file:
        for barang in daftar_barang:
            file.write(f"{barang[0]}|{barang[1]}|{barang[2]}\n")
        return True

def admin_menu():
    while True:
        print("""\n===Selamat Datang Admin! Silakan pilih menu:===
1. Tambah Barang
2. Cek Stok Barang
3. Update Barang
4. Hapus Barang
5. Logout
        """)
        pilih = input("Masukkan pilihan Anda (1-5): ")
        
        if pilih == "1":
            print("\n===Tambah Barang===")
            while True:
                nama = input("Masukkan nama barang: ")

                try:
                    harga = int(input("Masukkan harga barang: "))
                    jumlah = int(input("Masukkan jumlah barang: "))

                    if harga < 0 or jumlah < 0:
                        print("Harga dan jumlah tidak boleh negatif!")
                        continue

                except ValueError:
                    print("Input tidak valid. Silakan masukkan angka.")
                    continue
  
                tambah_barang(nama, harga, jumlah)
                print("Barang berhasil ditambahkan!")
                
                lanjut = input("\nApakah Anda ingin menambahkan barang lagi? (y/n): ").lower()

                if lanjut != "y":
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")

        elif pilih == "2":
            cek_barang()

        elif pilih == "3":
            print("\n===Update Barang===\n")
            while True:
                nama_barang = input("Masukkan nama barang yang ingin diupdate: ").lower()

                try:
                    harga_baru = input("\nMasukkan harga baru: (Kosongkan jika tidak ingin mengubah harga)\n")
                    if harga_baru == "":
                        harga_baru = None
                    else:
                        harga_baru = int(harga_baru)

                    jumlah_baru = input("Masukkan jumlah baru: (Kosongkan jika tidak ingin mengubah jumlah)\n")
                    if jumlah_baru == "":
                        jumlah_baru = None
                    else:
                        jumlah_baru = int(jumlah_baru)

                    if harga_baru is None and jumlah_baru is None:
                        print("Minimal satu data harus diubah!")
                        continue
                        
                    if harga_baru is not None and harga_baru < 0:
                        print("Harga tidak boleh negatif!")
                        continue

                    if jumlah_baru is not None and jumlah_baru < 0:
                        print("Jumlah tidak boleh negatif!")
                        continue

                except ValueError:
                    print("Input tidak valid. Silakan masukkan angka.")
                    continue
                berhasil = update_barang(nama_barang, harga_baru, jumlah_baru)

                if berhasil:
                    print("Barang berhasil diupdate!")
                    lanjut = input("\nApakah Anda ingin mengupdate barang lagi? (y/n): ").lower()
                    if lanjut == "m":
                        break
                    else:
                        print("Pilihan tidak valid. Silakan coba lagi.")

        elif pilih == "4":
            print("\n===Hapus Barang===\n")
            while True:
                nama_barang = input("Masukkan nama barang yang ingin dihapus: ").lower()
                berhasil = hapus_barang(nama_barang)

                if berhasil:
                    print("Barang berhasil dihapus!")
                    lanjut = input("\nApakah Anda ingin menghapus barang lagi? (y/n): ").lower()
                    if lanjut != "y":
                        break
                else:
                    print("Barang tidak ditemukan. Silakan coba lagi.")
    
        elif pilih == "5":
            print("Logout berhasil!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
        
