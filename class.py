class Mobil:
    def __init__(self,merek,warna):
        self.merek = merek
        self.warna = warna

    def berjalan(self):
        print(self.merek, "sedang berjalan")

    def berhenti(self):
        print(self.merek, "berhenti")

mobil1 = Mobil("Toyota","Merah")
mobil2 = Mobil("Honda","Hitam")

print(mobil1.merek)
print(mobil1.warna)

# ganti warna
mobil1.warna = "Biru"

print(mobil2.merek)
print(mobil2.warna)

mobil1.berjalan()
mobil1.berhenti()

print(mobil1.warna)

# Contoh 1

class AkunTrading:
    def __init__(self, nama,saldo):
        self.nama = nama
        self.saldo = saldo
    def tampilkan_saldo(self):
        print("Nama: ", self.nama)
        print("Saldo: ", self.saldo)
    def deposit(self,jumlah):
        self.saldo += jumlah
        print("Deposit berhasil")

akun1 = AkunTrading("Ihsan", 1_000_000)
akun1.tampilkan_saldo()
akun1.deposit(500_000)
akun1.tampilkan_saldo()