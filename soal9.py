print("=== JENIS BELANJA ===")
print("1. Member")
print("2. NonMember")

kode = int(input("Masukan Kode anda:"))
total = int(input("Masukan total belanja:"))

match kode:
    case 1:
        print("Jenis pelanggan: Member")
        if total >= 100000:
            print("Selamat anda dapat diskon 10%")
        else:
            print("Tidak dapat diskon")
    case 2:
        print("Jenis pelanggan: Non Member")
        if total >= 100000:
            print("Anda dapat diskon 5%")
        else:
            print("anda tidak dapat diskon")
