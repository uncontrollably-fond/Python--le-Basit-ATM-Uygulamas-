print("""
              MERHABA, X BANK A HOŞ GELDİNİZ!

              LÜTFEN KARTINIZI TAKINIZ! 
""")

veri_tabanı = {"1. KART":
                   {"isim": "TOYOTA",
                    "soyisim": "CUPRA",
                    "şifre": 1111,
                    "bakiye": 100,
                    "kredi kartı borcu": 1,
                    "kredi borç tarihi": "20/5/2022", },

               "2. KART":
                   {"isim": "MAZDA",
                    "soyisim": "RX-7",
                    "şifre": 2222,
                    "bakiye": 50,
                    "kredi kartı borcu": 1,
                    "kredi borç tarihi": "20/1/2022"}
               }





hak_Sayısı = 3
hesap1 = dict(veri_tabanı["1. KART"])
hesap2 = dict(veri_tabanı["2. KART"])

while hak_Sayısı > 0:
    takılan_kart = int(input("LÜTFEN 4 HANELİ ŞİFRENİZİ GİRİNİZ: "))

    if hesap1["şifre"] == takılan_kart:
        print(f"Sayın {hesap1['isim']} {hesap1['soyisim']}, LÜTFEN YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ!")

        seç = int(input("""
                [1] ->BAKİYE SORGULAMA
                [2] ->PARA YATIRMA
                [3] ->PARA ÇEKME
                [4] ->KREDİ KARTI BORCU SORGULAMA
                [5] ->BORÇ TARİHİ SORGULAMA\n"""))

        if seç == 1:
            print(f" BAKİYENİZ {hesap1['bakiye']} TL DİR. ")

        elif seç == 2:
            yatırılan = int(input("YATIRMAK İSTEDİĞİNİZ MİKTAR?: "))
            artan_Bakiye = hesap1["bakiye"] + yatırılan
            print(
                f" İŞLEM TAMAMLANDI!\nYATIRDIĞINIZ MİKTAR {yatırılan} TL DİR. YENİ BAKİYENİZ {artan_Bakiye} TL OLMUŞTUR.\n İYİ GÜNLER DİLERİZ!")


        elif seç == 3:
            çekilen = int(input("ÇEKMEK İSTEDİĞİNİZ MİKTAR?: "))
            azalan_Bakiye = hesap1["bakiye"] - çekilen
            print(
                f" İŞLEM TAMAMLANDI!\n ÇEKTİĞİNİZ MİKTAR {çekilen} TL DİR. YENİ BAKİYENİZ {azalan_Bakiye} TL OLMUŞTUR. \n İYİ GÜNLER DİLERİZ! ")


        elif seç == 4:
            print(f" KREDİ BORCUNUZ {hesap1['kredi kartı borcu']} TL DİR.")

        elif seç == 5:
            print(f" BORÇ TARİHİNİZ {hesap1['kredi borç tarihi']} DİR. ")

        break


    elif hesap2["şifre"] == takılan_kart:
        print(f"Sayın {hesap2['isim']} {hesap2['soyisim']}! LÜTFEN YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ!")
        seç = int(input("""
                [1] ->BAKİYE SORGULAMA
                [2] ->PARA YATIRMA
                [3] ->PARA ÇEKME
                [4] ->KREDİ KARTI BORCU SORGULAMA
                [5] ->BORÇ TARİHİ SORGULAMA\n"""))
        if seç == 1:
            print(f" BAKİYENİZ {hesap2['bakiye']} TL DİR. ")

        elif seç == 2:
            yatırılan = int(input("YATIRMAK İSTEDİĞİNİZ MİKTAR?: "))
            artan_Bakiye = hesap2["bakiye"] + yatırılan
            print(
                f" İŞLEM TAMAMLANDI!\nYATIRDIĞINIZ MİKTAR {yatırılan} TL DİR. YENİ BAKİYENİZ {artan_Bakiye} TL OLMUŞTUR.\n İYİ GÜNLER DİLERİZ!")


        elif seç == 3:
            çekilen = int(input("ÇEKMEK İSTEDİĞİNİZ MİKTAR?: "))
            azalan_Bakiye = hesap2["bakiye"] - çekilen
            if azalan_Bakiye < 0:
                print("YETERSİZ BAKİYE!!!")
            else:
                print(
                    f" İŞLEM TAMAMLANDI!\n ÇEKTİĞİNİZ MİKTAR {çekilen} TL DİR. YENİ BAKİYENİZ {azalan_Bakiye} TL OLMUŞTUR. \n İYİ GÜNLER DİLERİZ! ")


        elif seç == 4:
            print(f" KREDİ BORCUNUZ {hesap2['kredi kartı borcu']} TL DİR.")

        elif seç == 5:
            print(f" BORÇ TARİHİNİZ {hesap2['kredi borç tarihi']} DİR. ")

        break

    else:
        hak_Sayısı -= 1
        if hak_Sayısı == 0:
            print("                                  3 HAKKINIZ DA TÜKENMİŞTİR, KARTINIZ BLOKE OLDU!")
            exit()  