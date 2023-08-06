# sayı tahmin oyunu

import random 
import time

print("""********************************************
      
            SAYI TAHMİN OYUNU
      
********************************************""")

print("\n\n1 ile 40 arasında sayıyı tahmin edin..\n\n")

rastgele_sayı = random.randint(1,40)
tahmin_hakkı=7

while(True):
    tahmin=int(input("Tahmininiz: "))
    if(tahmin<rastgele_sayı):
        print("Bilgiler sorgulanıyor..")
        time.sleep(1)
        print("Daha yüksek bir sayı söyleyin!!\n")
        tahmin_hakkı-=1
    elif(tahmin>rastgele_sayı):
        print("Bilgiler sorgulanıyor..")
        time.sleep(1)
        print("Daha düşük bir sayı söyleyin!!\n")
        tahmin_hakkı-=1
    elif(tahmin==rastgele_sayı):
        print("Bilgiler sorgulanıyor..")
        time.sleep(1)
        print("Tebrikler!! Sayımız --> ",rastgele_sayı)
        break
    if(tahmin_hakkı==0):
        print("\n\nTahmin Hakkınız Bitti..!")
        print("Sayınız -> ",rastgele_sayı)