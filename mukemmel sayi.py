print("""
	====================
	MUKEMMEL SAYI HESABI
	====================
    *sayıları görmek için 'i' yazın
    *cikmak icin 'q' yazın
    """)
while True:
    deger = input("lutfen degeri girin:")
    bolenler =list()
    toplam =0
    if deger == 'i':
        print("Mukemmel sayi degerleri : 6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008139952128, 2658455991569831744654692615953842176,")
    
    elif deger == 'q':
        print("CIKIS YAPILIYOR...")
        break

    else:
        deger = int(deger)
        for hafiza in range(1,deger):
            if deger % hafiza == 0:
                    bolenler.append(hafiza)

        for hafiza1 in bolenler:
            toplam += hafiza1
                
        if deger ==toplam :
                print("girilen deger mukemmel sayidir")
            
        else:
                print("girilen deger mukemmel sayi degildir")
