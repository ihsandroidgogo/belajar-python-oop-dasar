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

# Contoh super()

class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

    def info(self):
        return f"{self.nama} - Gaji: Rp{self.gaji:,}"

class Manajer(Karyawan):
    def __init__(self, nama, gaji, tim):
        super().__init__(nama, gaji)   # panggil __init__ parent
        self.tim = tim                 # atribut tambahan

    def info(self):
        dasar = super().info()         # pakai hasil method parent
        return f"{dasar} | Anggota tim: {self.tim}"

m = Manajer("Ihsan", 15000000, 8)
print(m.info())

# Multiple Inheritance
class Terbang:
    def terbang(self):
        print("Terbang tinggi")

class Berenang:
    def berenang(self):
        print("Berenang cepat")

class Bebek(Terbang, Berenang):
    pass

b = Bebek()
b.terbang()
b.berenang()

# Multilevel Inheritance
class Kendaraan:
    def jalan(self):
        print("Kendaraan berjalan")

class Mobil(Kendaraan):
    def klakson(self):
        print("Tin tin!")

class MobilListrik(Mobil):
    def charge(self):
        print("Mengisi baterai")

x = MobilListrik()
x.jalan()     # dari Kendaraan
x.klakson()   # dari Mobil
x.charge()    # milik sendiri

# Contoh Ketiga

class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def harga_akhir(self):
        return self.harga

class ProdukDiskon(Produk):
    def __init__(self, nama, harga, diskon):
        super().__init__(nama, harga)
        self.diskon = diskon   # dalam persen

    def harga_akhir(self):
        return self.harga * (1 - self.diskon / 100)

items = [Produk("Nasi Goreng", 25000), ProdukDiskon("Es Teh", 8000, 25)]

for i in items:
    print(f"{i.nama}: Rp{i.harga_akhir():,.0f}")