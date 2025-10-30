#tugas 2 praktikum algoritma Pak Anung modul 2
#faradina kusuma, 065002500035
'''
Buatlah program untuk menghitung Tiket Masuk Kebun Binatang Berdasarkan Umur beserta Pembayarannya dengan aturan sebagai berikut: (Exercise 67)
●	Umur yang kurang dari atau sama dengan 2 tahun digratiskan
●	Umur yang lebih dari atau sama dengan 3 tahun hingga umur yang kurang dari atau sama dengan 12 tahun seharga 14 dollar
●	Umur lebih dari atau sama dengan 65 tahun seharga 18 dollar
●	Dan selain ketiga kategori diatas harganya normal yaitu 23 dollar
Program harus menggunakan perulangan untuk menghitung total keseluruhan harga yang diinputkan secara berulang, dan juga jika uang yang diinputkan berlebih maka program wajib mengembalikan nilai kembalian uang tersebut.
'''
total_harga = 0

while True:
  umur = (input("Masukkan umur pengunjung: "))
  if umur == '':
        break

  harga_tiket = 0

  umur = int(umur)
  if umur <= 2:
    harga_tiket = 0
    print(f"Harga tiket masuk kebun binatang adalah: ${harga_tiket:.2f}")
  elif 3 <= umur <= 12:
    harga_tiket = 14
    print(f"Harga tiket masuk kebun binatang adalah: ${harga_tiket:.2f}")
  elif umur >= 65:
    harga_tiket = 18
    print(f"Harga tiket masuk kebun binatang adalah: ${harga_tiket:.2f}")
  else:
    harga_tiket = 23
    print(f"Harga tiket masuk kebun binatang adalah: ${harga_tiket:.2f}")
  total_harga += harga_tiket
    
print(f"Total harga tiket masuk kebun binatang adalah: ${total_harga:.2f}")
uang_bayar = int(input("Masukkan jumlah uang yang dibayarkan: $"))


if uang_bayar < total_harga:
    print("Uang yang dibayarkan tidak cukup.")
else:
    kembalian = uang_bayar - total_harga
    print(f"Kembalian: ${kembalian:.2f}")
# Program untuk soal diatas menghitung tiket masuk kebun binatang berdasarkan umur dan pembayaran. pake perulangan if,elif,else.
