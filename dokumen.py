"Berisi fungsi membuka dan menyimpan kontak"


def membuka_kontak(path='D:/Data_Pribadi/Belajar_Python_2025/managemen_kontak/kotak.txt'):
    with open(path, mode='r') as file:
        kontak= file.readlines()
    return kontak

def meyimpan_kontak(path='D:/Data_Pribadi/Belajar_Python_2025/managemen_kontak/kotak.txt', isi=[]):
    with open(path, mode='w') as file:
        file.writelines(isi)