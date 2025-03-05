import random
import main, libs
from time import sleep

def start():
    skor = 0
    while True:
        bentuk_goa = "|_|"

        goa_kosong = [bentuk_goa] * 4
        goa = goa_kosong.copy()

        menang = random.randint(1, 4)
        goa[menang - 1] = "|$$|"

        goa_kosong = " ".join(goa_kosong)
        goa = " ".join(goa)

        print(f"\nLihat Goa Di Bawah Ini \n{goa_kosong}")

        angka = int(input("\nMasukkan angka[1..4]: "))

        while angka < 1 or angka > 4:
            angka = int(input("\nMasukkan angka[1..4]: "))
        if angka == menang:
            skor += 1
            print(f"\nSelamat Anda Menang \n{goa}")
            print(f"Skor Anda: {skor}")
        else:
            print(f"\nMaaf Anda Kalah \n{goa}")
            print(f"Skor Anda: {skor}")
        
        main_lagi = input("\nMain Lagi? (y/n): ")
        if main_lagi == "n":
            print(f"\nSkor Akhir: {skor}")
            libs.keluar()
            
if __name__ == "__main__":
    start()