"""Program Manajemen Kontak"""

kontak1 = {'nama' : 'Andi', 'HP' : 10984677, 'email' : 'andi@gmail.com'}
kontak2 = {'nama' : 'Ani', 'HP' : 10984675, 'email' : 'ani@gmail.com'}
kontak = [kontak1, kontak2]

while True:
    print("\nMenu Kotak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input("Masukan pilihan menu kontak (1,2,3, atau 4): ")

    if pilihan == '1':
        # melihat semua kontak
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f"\n{num}, {item['nama']}, {item['HP']}, {item['email']} ")
        else:
            print("Kontak Kosong")

    elif pilihan == '2':
        # menambahkan kontak
        nama = input("Masukkan nama kontak yang baru: ")
        HP = input("Masukan nomor kontak yang baru: ")
        email = input("Masukkan email kontak yang baru: ")
        kontak_baru = {'nama' : nama, 'HP': HP, 'email':email}
        kontak.append(kontak_baru)
        print(f"Kontak {kontak_baru['nama']} baru berhasil ditambahkan")
    elif pilihan == '3':
        # menghapus kontak
        print("\n")
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f"\n{num}, {item['nama']}, {item['HP']}, {item['email']} ")
        else:
            print("Kontak Kosong")
            continue

        index_hapus = int(input("Masukan nomor kontak yang akan dihapus: "))
        print(f"Kontak {index_hapus} berhasil dihapus")
        del kontak[index_hapus - 1]
    elif pilihan == '4':
        # keluar dari kontak
        break
    else:
        print("Anda memasukkan pilihan yang salah")