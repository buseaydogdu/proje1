import moduller.burclar
def aylarmenu():   
        print("\033[1;32;40m")
        #print("╔"+"═"*20+"╗")
        print("╔═════════════════════╗")
        print("║\033[1;31;40m   AYLAR           \033[1;32;40m  ║")
        print("║                     ║") 
        print("║  1-Ocak             ║")
        print("║  2-Şubat            ║")
        print("║  3-Mart             ║")
        print("║  4-Nisan            ║")
        print("║  5-Mayis            ║")
        print("║  6-Haziran          ║")
        print("║  7-Temmuz           ║")
        print("║  8-Ağustos          ║")
        print("║  9-Eylül            ║")
        print("║  10-Ekim            ║")
        print("║                     ║")
        print("║    Seçimiz nedir?   ║")
        print("╚═════════════════════╝")

        secim=input("Seçiminiz nedir?")

        if secim == "1":
                print("Ocak ayını seçtiniz")
                moduller.burclar.burclarmenu()
        if secim == "2":
                print("Şubat ayını seçtiniz")