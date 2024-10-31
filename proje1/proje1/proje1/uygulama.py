import uygulamalar.uygulamalarmenu
def uygulamamenu():
    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║\033[1;31;40m   UYGULAMALAR     \033[1;32;40m  ║")
    print("║                     ║")
    print("║  1-Hesap makinesi   ║")
    print("║  2-Çizimler         ║")
    print("║  3-Takvim           ║")
    print("║  4-Oyunlar          ║")
    print("║  5-Burçlar          ║")
    print("║  6-Renkler          ║")
    print("║  7-                 ║")
    print("║  8-                 ║")
    print("║  9-                 ║")
    print("║  10-                ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")

    if secim =="1":
        print("Hesap makinesini seçtiniz")
        uygulamalar.hesapmakinesi()
        uygulamamenu
    elif secim == "2":
        print("Çizimler kategorisini seçtiniz") 
    elif secim == "3":
        print("Takvim kategorisini seçtiniz")
        
