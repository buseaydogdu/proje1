def burcmenu():
    print("\033[1;32;40m")
    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║\033[1;31;40m  BURÇLAR    \033[1;32;40m  ║")
    print("║                     ║")
    print("║  1-Oğlak            ║")
    print("║  2-Kova             ║")
    print("║  3-Balik            ║")
    print("║  4-Koç              ║")
    print("║  5-Boğa             ║")
    print("║  6-İkizler          ║")
    print("║  7-Yengeç           ║")
    print("║  8-Aslan            ║")
    print("║  9-Terazi           ║")
    print("║  10-Akrep           ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")

    secim = input("Seçiminiz nedir?")

    if secim == "1":
        oglak()
    elif secim == "2":
        kova()
    elif secim == "3":
        balik()
    elif secim == "4":
        koc()
    elif secim == "5":
       boga()
    elif secim == "6":
        ikizler()
    elif secim == "7":
        yengec()
    elif secim == "8":
        aslan()
    elif secim == "9":
        terazi()    
    else:
        akrep()