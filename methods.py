# Contoh 1

class Menu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def beri_diskon(self, persen):      # instance method
        self.harga = self.harga * (1 - persen / 100)

m = Menu("Nasi Goreng", 25000)
m.beri_diskon(10)
print(m.harga)   # 22500.0