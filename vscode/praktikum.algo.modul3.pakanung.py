#algo.modul.3
#faradina kusuma
#065002500035

harga = int(input("Masukkan harga barang: "))
kupon = input("Apakah anda memiliki kupon? y/n: ")

harga_total = harga

#jika ada kupon
if kupon == 'y':
    diskon = input("Masukan kode kupon: ")
    if diskon == "IKL6309":
        diskon = 1
        potongan = harga * diskon
        harga = harga - potongan
        print("Selamat! anda mendapatkan diskon 100%")
    else: 
        print("Kode kupon salah atau expired")
        diskon = 0
        potongan = 0

#jika tidak ada kupon
elif kupon == 'n':
     if 40000 <= harga <= 89999:
            diskon = 0.2
     elif 90000 <= harga <= 189999:
        diskon = 0.4
     elif 190000 <= harga <= 389999:
        diskon = 0.6
     elif harga >= 390000:
        diskon = 0.8
     else:
        diskon = 0
potongan = harga * diskon
harga = harga - potongan

    
print("===================================")
print("Harga yang harus dibayar: ", harga_total)
print(f"diskon yang didapat:{int(diskon*100)}% ")
print(f"Total bayar: {int(harga)}")
print("Terima kasih telah berbelanja di toko kami")