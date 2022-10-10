"""
MUZIK KURSU OTOMASYONU

"""

kurs_sozlugu = {'1':"piyano_1 (Kurs -> piyano / seviye -> 1)",
                '2':"piyano_2 (Kurs -> piyano / seviye -> 2)",
                '3':"piyano_3 (Kurs -> piyano / seviye -> 3)",
                '4':"keman_1 (Kurs -> keman / seviye -> 1)",
                '5':"keman_2 (Kurs -> keman / seviye -> 2)",
                '6':"keman_3 (Kurs -> keman / seviye -> 3)",
                '7':"gitar_1 (Kurs -> gitar / seviye -> 1)",
                '8':"gitar_2 (Kurs -> gitar / seviye -> 2)",
                '9':"gitar_3 (Kurs -> gitar / seviye -> 3)"}


def ogrenci_ekle():
    print("Kayit islemine hos geldiniz :)")
    dosya = open("20010011040.txt", "a")
    ad = input("Lutfen ogrencinin adini giriniz: ")
    soyad = input("Lutfen ogrencinin soyadini giriniz: ")
    yas = input("Lutfen ogrencinin yasini giriniz: ")
    kurs_listele()
    while 1:
        ksec = int(input("Lutfen ogrencinin kaydolmak istedigi kursu seciniz:"))
        if ksec >= 1 and ksec <= 9:
            ksec = str(ksec)
            kurs = kurs_sozlugu[ksec]
            break
        else:
            print("Hatali kurs secimi! Tekrardan; ")
    aktar = ad + ' ' + soyad + ' ' + yas + ' ' + '- KURSU: ' + kurs + '\n'
    dosya.write(aktar)
    dosya.close()
    print("\nOgrenci eklendi.")


def ogrenci_ara():
    dosya = open("20010011040.txt", "r")
    arama_listesi = dosya.readlines()
    max = len(arama_listesi)
    ara_id = int(input("\n1 ile {} arasinda bilgilerini almak istediginiz ogrencinin id numarasini giriniz: ".format(max)))

    if ara_id > 0 and ara_id <= max:
        aranan_ogr = arama_listesi[ara_id-1]
        print("\nAradiginiz ogrencinin bilgileri:", aranan_ogr)
    else:
        print("\nBu id numarasinda herhangi bir ogrenci kayitli degil!")


def ogrenci_bilgi_guncelle():
    ogrenci_listele()
    dosya = open("20010011040.txt", "r+")
    guncelleme_listesi = dosya.readlines()
    max = len(guncelleme_listesi)
    gunc_id = int(input("1 ile {} arasinda bilgilerini guncellemek istediginiz ogrencinin id numarasini giriniz: ".format(max)))
    if gunc_id > 0 and gunc_id <= max:
        ad = input("Lutfen ogrencinin guncel adini giriniz: ")
        soyad = input("Lutfen ogrencinin guncel soyadini giriniz: ")
        yas = input("Lutfen ogrencinin guncel yasini giriniz: ")
        kurs_listele()
        while 1:
            ksec = int(input("Lutfen ogrencinin kaydolmak istedigi kursu seciniz:"))
            if ksec >= 1 and ksec <= 9:
                ksec = str(ksec)
                kurs = kurs_sozlugu[ksec]
                break
            else:
                print("Hatali kurs secimi! Tekrardan; ")
        guncelleme_listesi[gunc_id-1] = ad + ' ' + soyad + ' ' + yas + ' ' + kurs + '\n'
        print("\nOgrencinin bilgileri guncellendi.\n")
        guncel_dosya = open("20010011040.txt", "w")
        for i in guncelleme_listesi:
                guncel_dosya.write(i)
        guncel_dosya.close()
        # print("GUNCEL OGRENCI LISTESI")
        # ogrenci_listele()
    else:
        print("\nBu id numarasinda herhangi bir ogrenci kayitli degil!")


def ogrenci_sil():
    ogrenci_listele()
    dosya = open("20010011040.txt", "r")
    ogr_liste = dosya.readlines()
    dosya.close()
    # print(ogr_liste)
    sil_id = int(input("Silinecek ogrenci id numarasini giriniz:"))
    # print("Silinecek ogrenci id: ", sil_id)
    if sil_id > len(ogr_liste) or sil_id < 1:
        print("Bu id numarasinda herhangi bir ogrenci kayitli degil!")
    else:
        sil_ogr = ogr_liste[sil_id-1]
        # print("Silinecek ogrenci bilgileri: ", sil_ogr)
        dosya = open("20010011040.txt", "r+")
        dosya.seek(0)
        for i in ogr_liste:
            if i != sil_ogr:
                dosya.write(i)
        dosya.truncate()
        dosya.close()
        print("\nOgrenci silindi.")


def ogrenci_listele():
    dosya = open("20010011040.txt", "r")
    uzunluk = dosya.readlines()
    print("\n*KAYITLI OGRENCILERIMIZ*")
    dosya.seek(0)
    i = 0
    for _ in range(len(uzunluk)):
        i += 1
        print(str(i) + '- ' + dosya.readline(), end="")
    dosya.close()
    print("\nOgrencilerin tamami listelendi.\n")


def kurs_listele():
    print("*KURSLARIMIZ*")
    j = 0
    for i in range(1, len(kurs_sozlugu)+1):
        j += 1
        i = str(i)
        print("{}- ".format(j), kurs_sozlugu[i])


def kurs_fiyat():
    yas_bilg = int(input("\nFiyatlandirma icin yas girilmesi gerekmektedir!\nYas giriniz:"))
    fiyat1 = 150
    fiyat2 = 300
    fiyat3 = 450
    print("\nFiyatini ogrenmek istediginiz kursu seciniz:")
    kurs_listele()
    fiyat_kurs = input("Seciminiz: ")

    if fiyat_kurs == '1' or fiyat_kurs == '4' or fiyat_kurs == '7':
        if yas_bilg <= 20 or yas_bilg >= 65:
            print("Aylik kurs fiyati:", fiyat1-50)
        else:
            print("Aylik kurs fiyati:", fiyat1)

    elif fiyat_kurs == '2' or fiyat_kurs == '5' or fiyat_kurs == '8':
        if yas_bilg <= 20 or yas_bilg >= 65:
            print("Aylik kurs fiyati:", fiyat2-50)
        else:
            print("Aylik kurs fiyati:", fiyat2)

    elif fiyat_kurs == '3' or fiyat_kurs == '6' or fiyat_kurs == '9':
        if yas_bilg <= 20 or yas_bilg >= 65:
            print("Aylik kurs fiyati:", fiyat3-50)
        else:
            print("Aylik kurs fiyati:", fiyat3)

    else:
        print("Kurs bulunamadi!")


control = '1'
print("\n***************************")
print("*MUZIK KURSUNA HOSGELDINIZ*")
print("***************************")
while control != '0':
    print("\t\t*---*----*")
    print("\t\t*ANA MENU*")
    print("\t\t*---*----*")
    print("Yapmak istediginiz islemi seciniz:")
    print(">Ogrenci eklemek icin 1 i")
    print(">Ogrenci aramak icin 2 yi")
    print(">Kayitli bilgi guncellemek icin 3 u")
    print(">Kayitli ogrenci silmek icin 4 u")
    print(">Kayitli ogrencileri listelemek icin 5 i")
    print(">Kurslarimizi goruntulemek icin 6 yi")
    print(">Kurs fiyat hesabi icin 7 yi")
    print(">Cikis icin 0 i")
    secim = input("tuslayiniz->")

    if secim == '1':
        ogrenci_ekle()

    elif secim == '2':
        ogrenci_ara()

    elif secim == '3':
        ogrenci_bilgi_guncelle()

    elif secim == '4':
        ogrenci_sil()

    elif secim == '5':
        ogrenci_listele()

    elif secim == '6':
        kurs_listele()

    elif secim == '7':
        kurs_fiyat()

    elif secim == '0':
        exit()

    else:
        print("\nHatali karakter girdiniz!")

    control = input("\nAna menuye donmek icin 0 haric bir tus, cikis icin 0 i tuslayiniz: ")
