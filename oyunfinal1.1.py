import numpy as np
import random

# Oyun tahtasını oluştur
oyunplatformu = np.array([
    ["a", "z", "x", "x", "z", "x"],
    ["x", "x", "z", "x", "x", "z"],
    ["x", "z", "r", "z", "x", "x"],
    ["z", "x", "x", "x", "z", "x"],
    ["x", "r", "z", "r", "x", "z"],
    ["r", "z", "x", "z", "x", "x"],
    ["z", "x", "x", "x", "z", "x"],
    ["x", "x", "z", "r", "x", "z"],
    ["x", "z", "x", "z", "x", "x"],
    ["z", "x", "x", "x", "z", "x"]
])
oyunplatformu = oyunplatformu.reshape(10, 6)

# Oyun oynama adımları (30 rastgele adım)
oyun_oynama_adimlari = np.array([random.choice(["R", "U", "L", "D"]) for _ in range(30)])

# Oyuncunun başlangıç pozisyonu ve puanı
oyuncu_pozisyonu = [0, 0]  
oyuncu_puanı = 0

# Oyunu oynama
for yön in oyun_oynama_adimlari:
    satir, sutun = oyuncu_pozisyonu

    if yön == "L":
        if sutun - 1 < 0:
            print("Yanlış hamle: Sola gidemezsiniz!")
        else:
            hedef_hucre = oyunplatformu[satir, sutun - 1]
            if hedef_hucre == "z":
                oyuncu_puanı += 10
                print("Sola gidiliyor... Puanınız:", oyuncu_puanı)
            elif hedef_hucre == "r":
                oyuncu_puanı -= 10
                print("Sola gidiliyor... Puanınız:", oyuncu_puanı)
            elif hedef_hucre == "x":
                print("Sola gidiliyor...")
            else:
                print("Yanlış hamle: Sola gidemezsiniz!")
                continue
            oyunplatformu[satir, sutun] = "x"
            sutun -= 1
            oyunplatformu[satir, sutun] = "a"

    elif yön == "R":
        if sutun + 1 >= oyunplatformu.shape[1]:
            print("Yanlış hamle: Sağa gidemezsiniz!")
        else:
            hedef_hucre = oyunplatformu[satir, sutun + 1]
            if hedef_hucre == "z":
                oyuncu_puanı += 10
                print("Sağa gidiliyor... Puanınız:", oyuncu_puanı)
            elif hedef_hucre == "r":
                oyuncu_puanı -= 10
                print("Sağa gidiliyor... Puanınız:", oyuncu_puanı)
            elif hedef_hucre == "x":
                print("Sağa gidiliyor...")
            else:
                print("Yanlış hamle: Sağa gidemezsiniz!")
                continue
            oyunplatformu[satir, sutun] = "x"
            sutun += 1
            oyunplatformu[satir, sutun] = "a"

    elif yön == "U":
        if satir - 1 < 0:
            print("Yanlış hamle: Yukarı gidemezsiniz!")
        else:
            hedef_hucre = oyunplatformu[satir - 1, sutun]
            if hedef_hucre == "z":
                oyuncu_puanı += 10
                print("Yukarı gidiliyor... Puanınız:", oyuncu_puanı)
            elif hedef_hucre == "r":
                oyuncu_puanı -= 10
                print("Yukarı gidiliyor... Puanınız:", oyuncu_puanı)
            elif hedef_hucre == "x":
                print("Yukarı gidiliyor...")
            else:
                print("Yanlış hamle: Yukarı gidemezsiniz!")
                continue
            oyunplatformu[satir, sutun] = "x"
            satir -= 1
            oyunplatformu[satir, sutun] = "a"

    elif yön == "D":
        if satir + 1 >= oyunplatformu.shape[0]:
            print("Yanlış hamle: Aşağı gidemezsiniz!")
        else:
            hedef_hucre = oyunplatformu[satir + 1, sutun]
            if hedef_hucre == "z":
                oyuncu_puanı += 10
                print("Aşağı gidiliyor... Puanınız:", oyuncu_puanı)
            elif hedef_hucre == "r":
                oyuncu_puanı -= 10
                print("Aşağı gidiliyor... Puanınız:", oyuncu_puanı)
            elif hedef_hucre == "x":
                print("Aşağı gidiliyor...")
            else:
                print("Yanlış hamle: Aşağı gidemezsiniz!")
                continue
            oyunplatformu[satir, sutun] = "x"
            satir += 1
            oyunplatformu[satir, sutun] = "a"

    # Oyuncunun yeni pozisyonunu güncelle
    oyuncu_pozisyonu = [satir, sutun]

# Son durumu yazdır
print("\nOyun Tahtasının Son Durumu:")
print(oyunplatformu)
print("Oyun Bitti! Toplam Puanınız:", oyuncu_puanı)