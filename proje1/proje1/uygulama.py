import moduller.aylar
import moduller.burclar
import moduller.cizimler
import moduller.hesapmak
import moduller.oyunlar
import moduller.renkler
import moduller.yazarlar

def uygulamamenu():
    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║\033[1;31;40m   UYGULAMALAR     \033[1;32;40m  ║")
    print("║                     ║")
    print("║  1-Hesap makinesi   ║")
    print("║  2-Çizimler         ║")
    print("║  3-Aylar            ║")
    print("║  4-Oyunlar          ║")
    print("║  5-Burçlar          ║")
    print("║  6-Renkler          ║")
    print("║  7-Yazarlar         ║")
    print("║  8-                 ║")
    print("║  9-                 ║")
    print("║  10-                ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")

secim = input("Seçiminiz nedir?")
    if secim =="1":
        print("Hesap makinesi uygulamasını seçtiniz")
        moduller.hesapmak.hesapmenu()
        uygulamamenu()
    elif secim =="2":
        print("Çizimler uygulamasını seçtiniz.")
        uygulamamenu()
    elif secim =="3":
        print("Aylar uygulmasını seçtiniz.")   
    elif secim =="4":
        print("Oyunlar uygulmasını seçtiniz.")   
    elif secim =="5":
        print("Burçlar uygulmasını seçtiniz.")   
    elif secim =="6":
        print("Renkler uygulmasını seçtiniz.")  
    else:
        print("Seçim sadece 1,2,3,4,5,6,7,8,9,10 olabilir.")
        uygulamamenu() 
        
        uygulamamenu() 
    

    
        
