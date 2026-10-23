def admin_menu():
    while True:
        print("""===Selamat Datang Admin! Silakan pilih menu:===
1. Tambah Barang
2. Cek Stok Barang
3. Update Barang
4. Hapus Barang
5. Logout
        """)
        pilih = input("Masukkan pilihan Anda (1-5): ")
        if pilih == "1":
            tambah_barang()
        elif pilih == "2":
            cek_stok_barang()
        elif pilih == "3":
            update_barang()
        elif pilih == "4":
            hapus_barang()
        elif pilih == "5":
            print("Logout berhasil!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
        
