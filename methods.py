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