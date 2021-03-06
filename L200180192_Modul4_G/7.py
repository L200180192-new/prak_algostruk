class Mahasiswa(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku

h0 = Mahasiswa("Wosoek", 100, "Sukoharjo", 240000)
h1 = Mahasiswa("Minhae", 133, "Sragen", 230000)
h2 = Mahasiswa("Riska", 192, "Surakarta", 250000)
h3 = Mahasiswa("Hangyul", 180, "Surakarta", 235000)
h4 = Mahasiswa("Seungyoun", 155, "Boyolali", 240000)
h5 = Mahasiswa("Yohan", 189, "Salatiga", 250000)
h6 = Mahasiswa("Seungwoo", 177, "Klaten", 245000)
h7 = Mahasiswa("Junho", 143, "Wonogiri", 245000)
h8 = Mahasiswa("Eunsang", 211, "Klaten", 245000)
h9 = Mahasiswa("Dohyun", 130, "Karanganyar", 270000)
h10 = Mahasiswa("Hyeongjun", 199, "Purwodadi", 265000)

Daftar = [h0, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10]

def binSeMass(kumpulan, target):
    temp = []
    low = 0
    high = len(kumpulan)-1
    while low <= high :
        mid = (high+low)//2
        if kumpulan[mid] == target:
            midKiri = mid-1
            while kumpulan[midKiri] == target:
                temp.append(midKiri)
                midKiri = midKiri-1
            temp.append(mid)
            midKanan = mid+1
            while kumpulan[midKanan] == target:
                temp.append(midKanan)
                midKanan = midKanan+1
            return temp
        elif target < kumpulan[mid]:
            high = mid-1
        else:
            low = mid+1
    return False

kumpulan = [2, 4, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]
print(binSeMass(kumpulan, 6))
