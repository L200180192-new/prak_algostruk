class MhsTIF(object):
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', nim ' + str(self.nim)\
            + '. Tinggal di ' + self.kota\
            + '. Uang saku Rp ' + str(self.uangSaku)\
            + '. tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.nim
    def ambilUangSaku(self):
        return self.uangSaku

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

h0.next = h1
h1.next = h2
h2.next = h3
h3.next = h4
h4.next = h5
h5.next = h6
h6.next = h7
h7.next = h8
h8.next = h9
h9.next = h10

Daftar = [h0, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10]

