"""Program Manajemen Kontak"""

class Kontak:
    def __init__(self):
        self.kontak = []


    def melihat_kotak(self):
        # melihat semua kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f"{num}, {item['nama']}, {item['HP']}, {item['email']} ")
        else:
            print("Kontak Kosong")
            return 1

    def menambah_kotak(self):
        # menambahkan kontak
        nama = input("Masukkan nama kontak yang baru: ")
        HP = input("Masukan nomor kontak yang baru: ")
        email = input("Masukkan email kontak yang baru: ")
        kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
        self.kontak.append(kontak_baru)
        print(f"Kontak {kontak_baru['nama']} baru berhasil ditambahkan")

    def menghapus_kontak(self):
        # menghapus kontak
        if self.melihat_kotak() == 1:
           return
        else:
            index_hapus = int(input("Masukan nomor kontak yang akan dihapus: "))
            print(f"Kontak {index_hapus} berhasil dihapus")
            del self.kontak[index_hapus - 1]

kontak_kantor = Kontak()
kontak_keluarga = Kontak()

while True:
    print("\nMenu Kotak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input("Masukan pilihan menu kontak (1,2,3, atau 4): ")

    if pilihan == '1':
        kontak_keluarga.melihat_kotak()

    elif pilihan == '2':
        kontak_keluarga.menambah_kotak()

    elif pilihan == '3':
        kontak_keluarga.menghapus_kontak()

    elif pilihan == '4':
        # keluar dari kontak
        break
    else:
        print("Anda memasukkan pilihan yang salah")