def oyunlarmenu():
    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║\033[1;31;40m  OYUNLAR          \033[1;32;40m  ║")
    print("║                     ║")
    print("║  1-Tetris           ║")
    print("║  2-Adam Asmaca      ║")
    print("║  3-Yılan            ║")
    print("║  4-Taş Kağıt Makas  ║")
    print("║  5-İsim Şehir Hayvan║")
    print("║  6-Saklambaç        ║")
    print("║  7-                 ║")             
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")

    secim = input("Seçiminiz nedir?")

    if secim == "1":
        tetris()
    elif secim == "2":
        adam_asmaca()
    elif secim == "3":
        yilan()
    elif secim == "4":
        tas_kagit_makas()
    elif secim == "5":
        isim_sehir_hayvan()
    else:
        saklambac()