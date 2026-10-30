# Contoh 1

class Menu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def beri_diskon(self, persen):      # instance method
        self.harga = self.harga * (1 - persen / 100)

    # Contoh Dunder (double underscore)
    def __str__(self):
        return f"{self.nama} (Rp.{self.harga:,})"

    # Panggil dunder 2
    def __repr__(self):
        return f"Menu({self.nama!r}, {self.harga})"

# Panggil Diskon
m = Menu("Nasi Goreng", 25000)
m.beri_diskon(10)
print(f"Selamat dapat Diskon jadi : Rp,{m.harga}")

# Panggil Dunder 
print(m)
print(repr(m)) 
print([m]) # <-- List

# Contoh Kedua 
class Keranjang:
    def __init__(self):
        self.items = []

    def tambah(self, nama, harga):
        self.items.append((nama, harga))

    def __len__(self):
        return len(self.items)

    def __getitem__(self, i):
        return self.items[i]

    def __str__(self):
        return f"Keranjang berisi {len(self)} item"

    def __add__(self, other):
        baru = Keranjang()
        baru.items = self.items + other.items
        return baru

k1 = Keranjang()
k1.tambah("Nasi Goreng", 25000)

k2 = Keranjang()
k2.tambah("Es Teh", 8000)

gabung = k1 + k2
print(gabung)       # Keranjang berisi 2 item
print(gabung[1])    # ('Es Teh', 8000)