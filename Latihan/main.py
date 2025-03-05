from games import TebakAngka, Gacha, Undian

def menu():
    print("\nSelamat Di Menu Utama")
    print("1. Tebak Angka")
    print("2. Gacha")
    print("3. Undian")
    print("4. Exit")
    pilih = int(input("\nMasukkan Pilihan: "))

    if pilih == 1:
        TebakAngka.start()
    elif pilih == 2:
        Gacha.start()
    elif pilih == 3:
        Undian.start()
    elif pilih == 4:
        exit()

if __name__ == "__main__":
    menu()
