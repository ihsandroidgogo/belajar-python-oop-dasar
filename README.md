# Belajar OOP Python

OOP (Object-Oriented Programming) adalah cara membuat program dengan mengelompokkan data dan fungsi ke dalam sebuah objek.

Dalam OOP, kita bisa membuat sebuah class sebagai cetakan dan object sebagai hasil dari cetakan tersebut.

Satu class bisa digunakan untuk membuat banyak objek dengan data yang berbeda.

Mari kita pahami bagian pentingnya.

A. __init__()

Ini adalah metode khusus yang otomatis dipanggil ketika objek baru dibuat. Biasanya digunakan untuk mengatur data awal objek.

B. self

self merujuk pada objek yang sedang digunakan.

**Atribut**

Atribut adalah data yang dimiliki objek.

Dalam contoh di atas:
- self.merek adalah atribut merek.
- self.warna adalah atribut warna.

**Membuat method di dalam class**
Class bukan hanya untuk menyimpan data. Class juga bisa memiliki fungsi yang disebut method.

Contohnya, mobil dapat berjalan dan berhenti.

Perbedaan fungsi biasa dan method:
- Fungsi biasa dibuat menggunakan def di luar class.
- Method dibuat di dalam class dan biasanya bekerja dengan data objek melalui self.


### Ringkasan 
Istilah	    Fungsi
class	    Membuat cetakan objek
object	    Hasil dari class
__init__()	Mengatur data awal objek
self	    Merujuk pada objek itu sendiri
attribute	Data yang dimiliki objek
method	    Fungsi yang berada di dalam class
pass	    Placeholder ketika belum ada kode

# Apa itu Inheritance?
Inheritance memungkinkan sebuah class (child/subclass) mengambil atribut dan method dari class lain (parent/superclass), sehingga kamu tidak perlu menulis kode yang sama berulang kali.

Ada dua istilah yang perlu kamu ingat:
- Parent class: class induk yang mewariskan atribut dan method.
- Child class: class anak yang menerima warisan dari parent class.

**Fungsi super()**

Kalau child punya atribut tambahan, gunakan super() untuk memanggil __init__ milik parent.

Ringkasan
Konsep	                    Fungsi
class Anak(Induk)	        Membuat pewarisan
Overriding	                Menimpa method parent di child
super()	                    Memanggil method/__init__ parent
Multiple inheritance        Mewarisi dari >1 parent
MRO	                        Urutan pencarian method
isinstance() / issubclass()	Mengecek hubungan class