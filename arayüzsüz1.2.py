global tahta
tahta = [" " for _  in range(9)]

def oyuncu_seçici():
    while True:
        oynayan_oyuncu = input("Oyuncu seçin (x/o):")
        if oynayan_oyuncu.lower() in ("x", "o"):
            return oynayan_oyuncu.lower()
        else:
            print("geçersiz oyuncu")

def kazanan_hamleler():
    for i in range(0,9,3):
        if tahta[i]== tahta[i+1]== tahta[i+2] != " ":
            return True
    for i in range(3):
        if tahta[i]== tahta[i+3]== tahta[i+6] != " ":
            return True
    if tahta[0]==tahta[4]==tahta[8]  != " " or tahta[2] ==tahta[4]==tahta[6]  != " ":
        return True
    return False

def yazi_tahtasi():
    for i in range(0, 9, 3):
        print(" | ".join(tahta[i:i+3]))
        if i < 6:
            print("_" * 9)

def oyun():
    global tahta
    tahta = [" " for _ in range(9)] 
    oynayan_oyuncu = oyuncu_seçici()
    while True:
        yazi_tahtasi()
        try:
            hamle= int(input(f"{oynayan_oyuncu} <---bu oyuncu oynuyor 0 den 8 e kadar herhangi bir sayı yazın:"))
            if 0<= hamle< 9 and tahta[hamle] == " ":
                tahta[hamle]= oynayan_oyuncu
                
                if kazanan_hamleler():
                    yazi_tahtasi()
                    print(f"{oynayan_oyuncu} kazandı ")
                    break
                elif " " not in tahta:
                    yazi_tahtasi()
                    print("berabere")
                    break
                oynayan_oyuncu = "o"if oynayan_oyuncu == "x" else"x"
            else:
                print("geçersiz hamle")
        except ValueError:
            print("geçersiz hamle")
    yazi_tahtasi()
    print("oyun bitti")
oyun()

while True:         
        devam = input("oyunu tekrar oynamak ister misiniz? (E/H):")
        if devam.lower() == "e":
            tahta = [" " for _ in range(9)]
            oynayan_oyuncu = "x"
            oyun()
        elif devam.lower() == "h":
            print("oyun bitti")
            break
        else:
                print("yanlış giriş yaptınız")     