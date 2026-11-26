print("=== KATEGORI UJIAN ===")
print("1. Teori")
print("2. Praktek")

kode = int(input("Masukan Kategori Ujian:"))
nilai = int(input("Masukan Nilai Anda:"))

match kode:
    case 1:
        print("Kategori : Teori")
        if nilai >= 75:
            print("Anda lulus")
        else:
            print("Anda ulang")
    case 2:
        print("Kategori : Praktek")
        if nilai >= 75:
            print("Anda lulus")
        else:
            print("Anda ulang")
    case _:
        print("Tidak valid")