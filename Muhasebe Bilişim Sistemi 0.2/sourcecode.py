"""
Muhasebe Sistemi 0.2

by: Oguzhan DUYAR oguzhan.duyar.ogresyus@gmail.com
General Public License v3.0.


"""

print('''
                    ###############################
                     Muhasebe Bilişim Sistemi 0.2
            by: Oguzhan DUYAR oguzhan.duyar.ogresyus@gmail.com
                      General Public License v3.0
                    ###############################
     Kullanım Klavuzu
1- Sadece rakamları kullanınız. Programda kesinlikle harf tuşlarını kullanmayınız.
2- Ondalıklı rakamlar için virgül yerine nokta kullanınız. 12.354,00 ( Yanlış ) 12354.00 ( Doğru )
3- Anamenüye geri dönmek için 0 giriniz.''')



while True:

    print('''
    ----------İşlem Menüsü-----------
            
    1) KDV Hariç Turardan Hesaplama
    
    2) KDV Dahil Turardan Hesaplama 
    
    3) Tevkifat ve Vergileri Hesaplama 
    
    4) Aritmetik Ortalama Hesaplama
    
    5) İhale Teminat Tutarı Hesaplama
    
    6) Kullanıcı Bilgisayar Bilgileri
    
    7) Zamanı Göster
    
    ''')
    islemno=int(input("İşlem numarasını giriniz. ="))

    if islemno == 1:


        while True:

            # KDV Hariç hesaplama BAŞLANGIÇ

            ft = float(input("\nKDV hariç fatura tutarını giriniz ="))

            print('''
            --------------------------------
            %01 KDV tutarı ={:.2f}
            %08 KDV tutarı ={:.2f}
            %18 KDV tutarı ={:.2f}
            ---------------------------------
            %01 KDV dahil tutar ={:.2f}
            %08 KDV dahil tutar ={:.2f}
            %18 KDV dahil tutar ={:.2f}
            ---------------------------------
            '''.format(ft * 0.01, ft * 0.08, ft * 0.18, ft * 1.01, ft * 1.08, ft * 1.18))

            # KDV Hariç hesaplama SON

            if ft == 0:
                break

    elif islemno == 2:

        while True:

            # KDV Dahil hesaplama BAŞLANGIÇ

            ft = float(input("\nKDV dahil fatura tutarını giriniz ="))

            print('''
            --------------------------------
            %01 KDV tutarı ={:.2f}
            %08 KDV tutarı ={:.2f}
            %18 KDV tutarı ={:.2f}
            ---------------------------------
            %01 KDV hariç tutar ={:.2f}
            %08 KDV hariç tutar ={:.2f}
            %18 KDV hariç tutar ={:.2f}
            ---------------------------------
            '''.format((ft / 1.01) * 0.01, (ft / 1.08) * 0.08, (ft / 1.18) * 0.18, ft / 1.01, ft / 1.08, ft / 1.18))

            # KDV Dahil hesaplama SON

            if ft == 0:
                break

    elif islemno == 3:

        while True:

            # Tevkifat ve Vergileri Hesaplama Başlangıç
            ft = float(input("\nİşin bedeli (KDV Hariç Tutar)="))
            kdvo = float(input("\nKDV oranı yüzde kaç ="))
            print('''
            ---- KDV Tevkifat Oranları ----
            3/10 Yapım işleri Kdv Tevkifat: {:.2f}
            5/10 Bakım,Onarım,Terzi,Yemek Kdv Tevkifat: {:.2f}
            9/10 Proje,Danışmanlık,iş gücü temini,özel güvenlik Kdv Tevkifat: {:.2f}

            -------Vergiler------
            Damga Vergisi (Binde 9,48): {:.2f}
            Karar Pulu Vergisi (Binde 5,69): {:.2f}

            ------Damga Vergisi Düşülmüş Tutar-------
            Damga vergisi düşülmüş tutar : {:.2f}

            '''.format((ft * kdvo / 100) * 3 / 10, (ft * kdvo / 100) * 5 / 10, (ft * kdvo / 100) * 9 / 10, ft * 0.00948,
                       ft * 0.00569, (ft * kdvo / 100) + ft - (ft * 0.00948)))

            # Tevkifat ve Vergileri Hesaplama SON

            if ft == 0:
                break

    elif islemno == 4:

        while True:

            # Aritmetik ortalama kodları
            input_string = input("\nHesaplanacak sayıları aralarında boşluk bırakarak yazın.\n\nSayılar: ")
            list = input_string.split()
            print("\nAritmetik Ortalama Sonucu")
            sum = 0
            for num in list:
                sum += float(num)
            ortason = sum / len(list)
            print("\nSayıların Toplamı = ", sum)
            print("\nAritmetik Ortalaması =  {:.2f}".format(ortason))

            # Aritmetik ortalama kodları SON

            if sum == 0:
                break


    elif islemno == 5:

        while True:

            # İhale teminat  hesaplama BAŞLANGIÇ

            ym = float(input("\nYaklaşık maliyeti giriniz :"))
            print('''
            -----------------------------+
            % 03 Geçici teminat :{:.2f}  +
            % 06 Kesin  teminat :{:.2f}  +
            -----------------------------+
            '''.format(ym * 0.03, ym * 0.06))

            if ym == 0:
                break

    elif islemno == 6:

        while True:

            print("\nBilgileriniz:")
            import getpass

            kullaniciAdi = getpass.getuser()
            print("Kullanici Adi:", kullaniciAdi)

            import socket

            bilgisayarAdi = socket.gethostname()
            print("Bilgisayar Adi:", bilgisayarAdi)
            bilgisayarIpAdresi = socket.gethostbyname(socket.gethostname())
            print("Bilgisayar IP Adresi:", bilgisayarIpAdresi)
            from uuid import getnode as get_mac

            mac = get_mac()
            print("Mac adresiniz (48 bitlik değerde)= ", mac)

            ym = float(input("\nAnamenüye dönmek için 0 giriniz ="))

            if ym == 0:
                break


    elif islemno == 7:

        while True:

            print("\nBulunduğunuz Zaman:")
            import datetime as dt
            import pytz

            timezone_nw = pytz.timezone('America/New_York')
            nw_datetime_obj = dt.datetime.now(timezone_nw)

            timezone_london = pytz.timezone('Europe/London')
            london_datetime_obj = nw_datetime_obj.astimezone(timezone_london)

            timezone_Istanbul = pytz.timezone('Europe/Istanbul')
            Istanbul_datetime_obj = nw_datetime_obj.astimezone(timezone_Istanbul)

            print('\nAmerica/New York:', nw_datetime_obj)
            print('\nEurope/London:', london_datetime_obj)
            print('\nEurope/Istanbul:', Istanbul_datetime_obj)

            ym = float(input("\nAnamenüye dönmek için 0 giriniz ="))

            if ym == 0:
                break


    else:
        print("\nGeçersiz işlem numarası..\n")