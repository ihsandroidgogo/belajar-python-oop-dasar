class Kendaraan():
    def __init__(self,merek):
        self.merek = merek

    def tampilkan_merek(self):
        print("Merek: ", self.merek)

class Mobil(Kendaraan): # <--- Tambahkan Kendaraan di sini (Inheritance)
    pass

mobil1 = Mobil("Toyota")
mobil1.tampilkan_merek()