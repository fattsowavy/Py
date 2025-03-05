import random
import main, libs
from time import sleep

def start():
    simbols = ["🍒", "🍋", "🔔", "⭐"]
    skor = 0
    money = 100
    
    print("*********************************")
    print("* Selamat Datang Di Mesin Gacha *")
    print(f"* Uang Anda: {money}                *")
    print("*********************************")
    input("\nTekan Enter Untuk Mulai: ")

    while money > 0:
        slot = [random.choice(simbols) for i in range(3)]

        print("Mesin Gacha: \n")
        for simbol in slot:
            print(simbol, end=" ", flush=True)
            sleep(0.5)


        if slot[0] == slot[1] == slot[2] == simbols[0]:
            skor += 50
            money += 30
            print("\nCherry it Up!")
            print(f"Skor Anda: {skor}")
            print(f"Uang Anda: {money}")
        elif slot[0] == slot[1] == slot[2] == simbols[1]:
            skor += 30
            money += 20
            print("\nFresh Lemonade!")
            print(f"Skor Anda: {skor}")
            print(f"Uang Anda: {money}")
        elif slot[0] == slot[1] == slot[2] == simbols[2]:
            skor += 20
            money += 15
            print("\nDingDong!")
            print(f"Skor Anda: {skor}")
            print(f"Uang Anda: {money}")
        elif slot[0] == slot[1] == slot[2] == simbols[3]:
            skor += 10
            money += 10
            print("\nStars!")
            print(f"Skor Anda: {skor}")
            print(f"Uang Anda: {money}")
        else:
            money -= 10
            print("\nMaaf Anda Kalah!")
            print(f"Skor Anda: {skor}")
            print(f"Uang Anda: {money}")
        
        again = input("\nApakah anda ingin gacha lagi? (y/n): ")
        if again != "y":
            kembali = input("\nApakah anda ingin kembali ke menu utama? (y/n): ")
            if kembali == "y":
                main.menu()
            else:
                exit()
        
        if money <= 0:
            libs.keluar()
            
if __name__ == "__main__":
    start()