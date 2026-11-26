usia = int(input("Masukkan usia pengunjung: "))

if usia >= 17:
    print("Pilih Genre Film:")
    print("1. Horor")
    print("2. Komedi")
    print("3. Keluarga")
    print("4. Aksi")

    genre = input("Pilih genre (1-4): ")

    if genre == "1":
        print("1. Horor Indonesia")
        print("2. Horor Luar Negeri")
        pilihan = input("Pilih film: ")

        if pilihan == "1":
            film = "Horor Indonesia"
        elif pilihan == "2":
            film = "Horor Luar Negeri"
        else:
            film = "Pilihan tidak valid"

    elif genre == "2":
        print("1. Komedi Indonesia")
        print("2. Komedi Luar Negeri")
        pilihan = input("Pilih film: ")

        if pilihan == "1":
            film = "Komedi Indonesia"
        elif pilihan == "2":
            film = "Komedi Luar Negeri"
        else:
            film = "Pilihan tidak valid"

    elif genre == "3":
        print("1. Keluarga Indonesia")
        print("2. Keluarga Luar Negeri")
        pilihan = input("Pilih film: ")

        if pilihan == "1":
            film = "Keluarga Indonesia"
        elif pilihan == "2":
            film = "Keluarga Luar Negeri"
        else:
            film = "Pilihan tidak valid"

    elif genre == "4":
        print("1. Hollywood")
        print("2. Indonesia")
        print("3. Bollywood")
        pilihan = input("Pilih film: ")

        if pilihan == "1":
            film = "Hollywood"
        elif pilihan == "2":
            film = "Indonesia"
        elif pilihan == "3":
            film = "Bollywood"
        else:
            film = "Pilihan tidak valid"

    else:
        film = "Pilihan tidak valid"

else:
    print("Pilih Jenis Animasi:")
    print("1. Animasi 2 Dimensi")
    print("2. Animasi 3 Dimensi")

    animasi = input("Pilih animasi (1-2): ")

    if animasi == "1":
        print("1. Naruto")
        print("2. One Piece")
        pilihan = input("Pilih film: ")

        if pilihan == "1":
            film = "Naruto"
        elif pilihan == "2":
            film = "One Piece"
        else:
            film = "Pilihan tidak valid"

    elif animasi == "2":
        print("1. Nemo")
        print("2. Kungfu Panda")
        pilihan = input("Pilih film: ")

        if pilihan == "1":
            film = "Nemo"
        elif pilihan == "2":
            film = "Kungfu Panda"
        else:
            film = "Pilihan tidak valid"

    else:
        film = "Pilihan tidak valid"

if film != "Pilihan tidak valid":
    print("Selamat Menyaksikan", film)
else:
    print("Pilihan tidak valid!")

