# Contoh 1

class Kendaraan():
    def __init__(self,merek):
        self.merek = merek

    def tampilkan_merek(self):
        print("Merek: ", self.merek)

class Mobil(Kendaraan): # <--- Tambahkan Kendaraan di sini (Inheritance)
    pass

mobil1 = Mobil("Toyota")
mobil1.tampilkan_merek()

# Method Overriding

class Hewan:
    def __init__(self,nama):
        self.nama = nama
    def makan(self):
        print(f"{self.nama} sedang makan")
    def bersuara(self):
        print("Contoh nya Kosong")

# Kucing mewarisi Hewan: tulis nama parent di dalam kurung
class Kucing(Hewan):
    def bersuara(self):
        print(f"{self.nama} Meong!")

# Menimpa method parent
class Anjing(Hewan):
    def bersuara(self):
        print(f"{self.nama}: Guk guk!")

# Cara Panggil
for hewan in [Anjing("Rex"), Kucing("Mona")]:
    hewan.bersuara()