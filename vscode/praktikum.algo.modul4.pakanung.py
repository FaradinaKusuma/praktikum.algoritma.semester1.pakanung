#modul.4 algoritma
# KAMIS 9/10/2025
# faradina kusuma 
# 065002500035

#latihan 1
#melakukan operasi perulangan dengan for
for i in range(7, 0, -1):
    for j in range(i):
        print(i, end="")
    print()

#latihan 2
#Buatlah program yang sebelumnya telah dibuat yang menentukan jumlah hari dalam
#suatu bulan sesuai dengan inputan bulan dan tahun yang diinputkan oleh user
#menggunakan implementasi perulangan while.

while True:
    if True:
        bulan = int(input("Masukkan bulan (1-12): "))
        if 1 <= bulan <= 12:
            break
        else:
            print("Bulan harus antara 1 sampai 12. Silakan coba lagi.")
     


tahun = int(input("Masukkan tahun: "))

if bulan in (1,3,5,7,8,10,12):
    hari = 31
elif bulan in (4,6,9,11):
    hari = 30
elif bulan == 2:
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        hari = 29
    else:
        hari = 28

print("Jumlah hari dalam bulan", bulan, "tahun", tahun, "adalah", hari)