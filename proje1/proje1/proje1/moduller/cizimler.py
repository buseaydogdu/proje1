import turtle

def kare():
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)

def ucgen():
    for x in range(3):
        turtle.forward(100)
        turtle.right(120)

def dikdortgen():
    for z in range(2):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)

def besgen():
    for y in range(5):
        turtle.forward(100)
        turtle.right(72)

def altigen():
    for k in range(6):
        turtle.forward(100)
        turtle.right(60)


def cizimmenu():
    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║\033[1;31;40m   ÇİZİMLER      \033[1;32;40m  ║")
    print("║                     ║")
    print("║  1-Kare             ║")
    print("║  2-Üçgen            ║")
    print("║  3-Dikdörtgen       ║")
    print("║  4-Beşgen           ║")
    print("║  5-Altıgen          ║")
    print("║  6-Çıkış (e)        ║")
    print("║                     ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")

    secim = input("Seçiminiz nedir?")

    if secim == "1" :
        kare()
    elif secim == "2" : 
        ucgen()
    elif secim == "3" : 
        dikdortgen()
    elif secim == "4" : 
        besgen()
    else : 
        altigen()