"Berisi kelas Kontak untuk menjalankan program kontak"

import dokumen

class Kontak:
    def __init__(self):
        self.kontak = dokumen.membuka_kontak()


    def melihat_kotak(self):
        # melihat semua kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f"{num}. " + item)
        else:
            print("Kontak Kosong")
            return 1

    def menambah_kotak(self):
        # menambahkan kontak
        nama = input("Masukkan nama kontak yang baru: ")
        HP = input("Masukan nomor kontak yang baru: ")
        email = input("Masukkan email kontak yang baru: ")
        kontak_baru = (f'{nama} {HP}, {email}' + '\n')
        self.kontak.append(kontak_baru)
        print(f"Kontak {nama} baru berhasil ditambahkan")

    def menghapus_kontak(self):
        # menghapus kontak
        if self.melihat_kotak() == 1:
           return
        else:
            try:
                index_hapus = int(input("Masukan nomor kontak yang akan dihapus: "))
                print(f"Kontak {index_hapus} berhasil dihapus")
                del self.kontak[index_hapus - 1]
            except:
                print("Inputa yang anda masukan salah ")

    def keluar_kontak(self):
        dokumen.meyimpan_kontak(isi=self.kontak)
