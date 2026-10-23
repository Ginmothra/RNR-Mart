import admin as adm
import kasir as kas

while True:
    print("""Selamat Datang di RNR Mart 🛒
1. Admin
2. Kasir
3. Exit
""")
    role = input("Ingin Login Sebagai? (1/2/3) \n")
    if role == "1":
        adm.admin_menu()
    elif role == "2":
        kas.kasir_menu()
    elif role == "3":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

