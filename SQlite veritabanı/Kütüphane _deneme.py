from Kütüphane import *
print(""""********************************
Kütüphane programına hoşgeldiniz.
İşlemler;
1. Kitapları Göster
2. Kitapları Sorgula
3. Kitap Ekle 
4. Kitap Sil
5. Baskı Yükselt
 
Çıkmak için q ya basınız 
**********************************
""")
kütüphane =Kütüphane()
while True:
    işlem =input("Yapacağınız İşlemi seçiniz : ")
    if(işlem=='q'):
        print("program sonlandırılıyor...")
        break

    elif(işlem=="1"):
        kütüphane.kitapları_göster()
    elif (işlem == "2"):
        isim=input("Hangi kitabı istiyorsunuz : ")
        print("Kitap sorgulanıyor...")
        time.sleep(1)
        kütüphane.kitap_sorgula(isim)
    elif (işlem == "3"):
        isim=input("İsim :")
        yazar = input("Yazar : ")
        yayınevi =input("Yayınevi : ")
        tür =input("Tür :")
        baskı= int(input("Baskı : "))
        yeni_kitap= Kitap(isim,yazar,yayınevi,tür,baskı)
        print("Kitap ekleniyor...")
        time.sleep(1)
        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitabınız başarıyla eklendi")



    elif (işlem == "4"):
        isim = input("Silmek istediğiniz kitabın adı")
        cevap=input("Emin misiniz? : (E/H)")
        if (cevap == 'E'):
            print("Kitabınız siliniyor...")
            time.sleep(1)
            kütüphane.kitap_sil(isim)
            print("Kitabınız silindi.")
        elif(cevap=='H'):
            continue
    elif(işlem=="5"):
        isim =input("Hangi kitabın baskısını yükseltmek istersiniz?")
        print("baskı yükseltiliyor..")
        time.sleep(1)
        kütüphane.baskı_yükselt(isim)
        print("baskı yükseltildi")
    else:
        print("Geçersiz işlem")