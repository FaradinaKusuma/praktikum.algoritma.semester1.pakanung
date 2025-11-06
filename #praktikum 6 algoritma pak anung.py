#praktikum 6 algoritma pak anung
#faradina kusuma, 065002500035
#membuat fungsi

# Fungsi untuk mengubah huruf mutu menjadi angka
def konversi_nilai(huruf):
    mapping = {
        "A": 4.00,
        "A-": 3.75,
        "B+": 3.50,
        "B": 3.00,
        "B-": 2.75,
        "C+": 2.50,
        "C": 2.00,
        "C-": 1.75,
        "D": 1.50,
        "E": 1.25
    }
    return mapping.get(huruf.upper(), None)

# Fungsi untuk menghitung rata-rata nilai huruf
def rata_rata_nilai(list_huruf):
    total = 0
    hitung = 0
    
    for huruf in list_huruf:
        nilai = konversi_nilai(huruf)
        if nilai is None:
            print(f"Nilai '{huruf}' tidak valid!")
            continue
        total += nilai
        hitung += 1
    
    if hitung == 0:
        return 0
    return total / hitung

# --- Program utama ---
nilai_input = input("Masukkan daftar nilai huruf (pisahkan dengan spasi): ")
daftar_nilai = nilai_input.split()

rata2 = rata_rata_nilai(daftar_nilai)
print(f"Rata-rata nilai: {rata2:.2f}")
