from Modul5 import *
class MhsTIF(object):
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', nim ' + str(self.nim)\
            + '. Tinggal di ' + self.kota\
            + '. Uang saku Rp ' + str(self.uangSalu)\
            + '. tiap bulannya.'
        return s

h0 = MhsTIF("Wosoek", 100, "Sukoharjo", 240000)
h1 = MhsTIF("Minhae", 133, "Sragen", 230000)
h2 = MhsTIF("Riska", 192, "Surakarta", 250000)
h3 = MhsTIF("Hangyul", 180, "Surakarta", 235000)
h4 = MhsTIF("Seungyoun", 155, "Boyolali", 240000)
h5 = MhsTIF("Yohan", 189, "Salatiga", 250000)
h6 = MhsTIF("Seungwoo", 177, "Klaten", 245000)
h7 = MhsTIF("Junho", 143, "Wonogiri", 245000)
h8 = MhsTIF("Eunsang", 211, "Klaten", 245000)
h9 = MhsTIF("Dohyun", 130, "Karanganyar", 270000)
h10 = MhsTIF("Hyeongjun", 199, "Purwodadi", 265000)

daftar = [h0, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10]

def urutkanNIM(list):
    NIM = []
    for i in list:
        NIM.append(i.nim)
        insertionSort(NIM)
    return NIM
