def transaksi(barang, jumlah, daftar_barang):
    with open ("storage/barang.txt", "r", encoding ="utf-8") as file:
        data_barang = file.readlines()

    try:
        jumlah = int(jumlah)
    except ValueError:
        print("Jumlah barang harus berupa angka.")
        return False

    if jumlah <= 0:
        print("Jumlah barang harus lebih dari 0.")
        return False

    for data in data_barang:
        nama, harga, stok = data.strip().split("|")
        
        if nama.lower() == barang.lower():
            if int(jumlah) <= 0:
                print("Jumlah barang harus lebih dari 0.")
                return False

            if int(jumlah) > int(stok):
                print("Stok tidak cukup. Stok tersedia:", stok)
                return False
            
            print(f"\nBarang {nama} berhasil ditambahkan ke keranjang.")

            daftar_barang.append((nama, int(harga), int(jumlah)))


            return True
        
    print("Barang tidak ditemukan.")
    return False

def sum_transaksi(daftar_barang):
    print("\n=== Ringkasan Transaksi ===")

    total_harga = 0

    for nama, harga, jumlah in daftar_barang:
        subtotal = harga * jumlah
        total_harga += subtotal
        print(f"{nama} - {jumlah} x {harga} = {subtotal}")

    print(f"Total Harga: {total_harga}")

def exec_transaksi(daftar_barang):
    with open("storage/barang.txt", "r", encoding="utf-8") as file:
        data_barang = file.readlines()

    jumlah_beli = {}

    for nama, harga, jumlah in daftar_barang:
        nama = nama.lower()
        jumlah_beli[nama] = jumlah_beli.get(nama, 0) + jumlah

    for data in data_barang:
        nama, harga, stok = data.strip().split("|")

        if nama.lower() in jumlah_beli:
            if jumlah_beli[nama.lower()] > int(stok):
                print(f"Stok tidak cukup untuk {nama}. Transaksi dibatalkan.")
                return False

    data_baru = []
    total_harga = 0

    for data in data_barang:
        nama, harga, stok = data.strip().split("|")

        if nama.lower() in jumlah_beli:
            stok = int(stok) - jumlah_beli[nama.lower()]

        data_baru.append(f"{nama}|{harga}|{stok}\n")

    for nama, harga, jumlah in daftar_barang:
        total_harga += harga * jumlah

    with open("storage/barang.txt", "w", encoding="utf-8") as file:
        file.writelines(data_baru)

    print("\nTransaksi berhasil!")
    print(f"Total Harga: {total_harga}")

    return True

# def diskon():

# def cetak_struk():

def kasir_menu():
    while True:
        print("""===Selamat Datang Kasir! Silakan pilih menu:===
1. Transaksi
2. Logout
        """)
        pilih = input("Masukkan pilihan Anda (1-2): ")
        if pilih == "1":
            daftar_barang = []

            while True:
                Barang = input("Masukkan nama barang yang ingin dibeli: ")
                Jumlah = input("Masukkan jumlah barang yang ingin dibeli: ")

                berhasil = transaksi(Barang, Jumlah, daftar_barang)
                if not berhasil:
                    continue
                lanjut = input("Apakah ingin menambah barang lain? (y/n)\n").lower()
                
                if lanjut == "y":
                    continue
                elif lanjut == "n":
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")

            if daftar_barang:
                sum_transaksi(daftar_barang)
                konfirmasi = input("Apakah sudah sesuai? (y/n)\n").lower()
                if konfirmasi == "y":
                    exec_transaksi(daftar_barang)
                elif konfirmasi == "n":
                    print("Transaksi dibatalkan.")
                else:
                    print("Pilihan tidak valid. Transaksi dibatalkan.")
            else:
                print("Tidak ada barang yang dibeli. Transaksi dibatalkan.")
                   
        elif pilih == "2":
            print("Logout berhasil!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# STRUK
def sum_transaksi(daftar_barang):
    print("\n=== Ringkasan Transaksi ===")
    total_harga = 0

    for nama, harga, jumlah in daftar_barang:
        subtotal = harga * jumlah
        total_harga += subtotal
        print(f"{nama}\n  {jumlah} x {harga:,} = {subtotal:,}".replace(',', '.'))

    persen_diskon, nominal_diskon = hitung_diskon(total_harga)
    total_bayar = total_harga - nominal_diskon

    print("-" * 30)
    print(f"Total awal     : Rp{total_harga:,}".replace(',', '.'))
    if persen_diskon > 0:
        print(f"Diskon ({persen_diskon}%)   : Rp{nominal_diskon:,}".replace(',', '.'))
    print(f"Total Bayar    : Rp{total_bayar:,}".replace(',', '.'))
    
    return total_harga, nominal_diskon, total_bayar

def cetak_struk(daftar_barang, total_awal, nominal_diskon, total_bayar, tunai, nama_kasir="Sinta"):
    kembalian = tunai - total_bayar
    waktu_sekarang = datetime.now().strftime("%d.%m.%Y %H:%M")
    
    print("\n" + "="*35)
    print("             Alfamart            ".center(35))
    print("      Belanja puas harga pas     ".center(35))
    print()
    print("          Alfamart Jogja         ".center(35))
    print("           Jl. Kenangan          ".center(35))
    print("              Jogja              ".center(35))
    print("           08897482739           ".center(35))
    print()
    print(f"{waktu_sekarang:<25} #281")
    print("-" * 35)

    for nama, harga, jumlah in daftar_barang:
        subtotal = harga * jumlah
        print(f"{nama}")
        print(f"  {jumlah}x {harga:,.0f}".replace(',', '.').ljust(22) + f"{subtotal:,.0f}".replace(',', '.').rjust(13))

    print("-" * 35)
    print(f"Total".ljust(20) + f"Rp{total_awal:,.0f}".replace(',', '.').rjust(15))
    if nominal_diskon > 0:
        print(f"Diskon".ljust(20) + f"-Rp{nominal_diskon:,.0f}".replace(',', '.').rjust(15))
        print(f"Total Bayar".ljust(20) + f"Rp{total_bayar:,.0f}".replace(',', '.').rjust(15))
    
    print(f"Tunai".ljust(20) + f"Rp{tunai:,.0f}".replace(',', '.').rjust(15))
    if kembalian > 0:
        print(f"Kembali".ljust(20) + f"Rp{kembalian:,.0f}".replace(',', '.').rjust(15))
    
    print(f"{'Lunas':>35}")
    print()
    print("Barang yang sudah dibeli tidak b".center(35))
    print("isa dikembalikan lagi".center(35))
    print()
    print(f"Kasir : {nama_kasir}".center(35))
    print()
    print("Terima kasih".center(35))
    print("="*35 + "\n")
