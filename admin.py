def tambah_barang(nama, harga, jumlah):
    with open ("storage/barang.txt", "a", encoding="utf-8") as file:
        file.write(f"{nama}|{harga}|{jumlah}\n")

def cek_barang():
    while True:
        with open("storage/barang.txt", "r", encoding="utf-8") as file:
            print("\n===Daftar Barang===")
            for barang in file:
                nama, harga, jumlah = barang.strip().split("|")
                print(f"Nama: {nama}, Harga: {harga}, Jumlah: {jumlah}")
        print("\nKembali ke menu sebelumnya? (y)")
        kembali = input("").lower()
        if kembali == "y":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


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
            update_barang()
        elif pilih == "4":
            hapus_barang()
        elif pilih == "5":
            print("Logout berhasil!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
        
