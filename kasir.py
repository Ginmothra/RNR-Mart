def kasir_menu():
    while True:
        print("""===Selamat Datang Kasir! Silakan pilih menu:===
1. Transaksi
2. Logout
        """)
        pilih = input("Masukkan pilihan Anda (1-2): ")
        if pilih == "1":
            transaksi()
        elif pilih == "2":
            print("Logout berhasil!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
