import random
from time import sleep
import main
import libs

def start():
    while True:
        jumlah = int(input("\nJumlah Nama yang akan dimasukkan: "))

        nama = []
        for i in range(jumlah):
            name = input(f"Masukkan nama ke - {i+1} : ")
            nama.append(name)
        
        menang = random.choice(nama)
        
        print()
        print(" | ".join(nama))

        print("\nPemenang Undian: \n")
        sleep(1)
        print("3...")
        sleep(1)
        print("2...")
        sleep(1)
        print("1...")
        sleep(2)
        
        print(f"\n** {menang} **")
        
        main_lagi = input("\nMain Lagi?[y/n]: ")
        if main_lagi == "n":
            libs.keluar()
            

if __name__ == "__main__":
    start()
