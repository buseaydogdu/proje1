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

    secim = input()

    if secim =="1":
        print("Hesap makinesi uygulamasını seçtiniz")
        moduller.hesapmak.hesapmenu()
        uygulamamenu()
    elif secim =="2":
        print("Çizimler uygulamasını seçtiniz.")
        moduller.cizimler.cizimmenu()
        uygulamamenu()
    elif secim =="3":
        print("Aylar uygulmasını seçtiniz.")
        moduller.aylar.aylarmenu()
        uygulamamenu()    
    elif secim =="4":
        print("Oyunlar uygulmasını seçtiniz.")
        moduller.oyunlar.oyunlarmenu()
        uygulamamenu()  
    elif secim =="5":
        print("Burçlar uygulmasını seçtiniz.")
        moduller.burclar.burcmenu()
        uygulamamenu()    
    elif secim =="6":
        print("Renkler uygulmasını seçtiniz.")
        moduller.renkler.renkmenu()
        uygulamamenu()    
    else :
        print("Yazarlar uygulmasını seçtiniz.")
        moduller.yazarlar.yazarmenu()
        uygulamamenu() 

uygulamamenu()
    

    
        
