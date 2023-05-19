# Penjelasan singkat
# Tanda pagar (#) tidak berpengaruh

# Tipe data pada Python yaitu:
# 01. Tipe text yaitu str (string)
# 02. Tipe angka yaitu int, float, dan complex
# 03. Tipe data majemuk yaitu list, tuple, set, dan range
# 04. Tipe data map yaitu dict

# type() digunakan untuk memeriksa tipe data pada variabel

# 01. Tipe Text
# Contoh Tipe Data string (teks)
string_text = "Hallo Dunia!"
print(string_text)
print(type(string_text))
print()  # untuk menambahkan baris baru

# 02. Tipe Angka
# Contoh Tipe Data integer (bilangan bulat)
integer_number = 2 # angka bilangan bulat (0 1 2 3 4 5 6 7 8 9) 
print(integer_number)
print(type(integer_number))
print()  # untuk menambahkan baris baru

# Contoh Tipe Data float (bilangan desimal)
float_number = 3.13
print(float_number)
print(type(float_number))
print()  # untuk menambahkan baris baru

# Contoh Tipe Data complex (gabunagan)
complex_number_1 = complex(1.5)
complex_number_2 = complex(2j)
print(complex_number_1)
print(complex_number_2)
print(type(complex_number_1))
print(type(complex_number_2))
print()  # untuk menambahkan baris baru

# 03. Tipe Data Majemuk
# Pake bahasa Indonesia aja coy, biar gampang :v
# Contoh Tipe Data list (daftar)
nama_siswa = ["Andi", "Budi", "Celi", "Doni"]
print(nama_siswa) # urutan dimulai dari 0 bukan 1
print(nama_siswa[0])
print(nama_siswa[1])
print(nama_siswa[2])
print(nama_siswa[3])
print(type(nama_siswa))
print()  # untuk menambahkan baris baru

# contoh tipe data dari tuple
mahasiswa = ("Nana", "Nini", "Nunu", "Nono")
print(mahasiswa)
print(mahasiswa[0])
print(mahasiswa[1])
print(nama_siswa[2])
print(nama_siswa[3])
print(type(mahasiswa))
print()  # untuk menambahkan baris baru

# contoh tipe data dari set
merk_mobil = {"Nissan", "BMW", "Toyota"}
print(merk_mobil)
# jika code dibawah dijalankan akan error karena
# tipe data set unsubcriptable (tidak berurutan)
# print(merk_mobil[1])
# jika code dibawah dijalankan akan error karena
# tipe data set unsubcriptable (tidak berurutan)
# print(merk_mobil[2])
print(type(merk_mobil))
print()  # untuk menambahkan baris baru

# contoh tipe data dari frozzenset
nama_desa = frozenset({"Pajajaran", "Majapahit", "Sriwijaya"})
print(nama_desa)
print(type(nama_desa))
print()  # untuk menambahkan baris baru

# contoh tipe data dari dict
detail_mobil = {"merek": "Toyota", "asal": "Jepang"}
print(detail_mobil)
print(detail_mobil["merek"])
print(detail_mobil["asal"])
print(type(detail_mobil))
print()  # untuk menambahkan baris baru

# contoh tipe data dari bytes
angka_bytes = bytes(12)
print(angka_bytes)
print(type(angka_bytes))
print()  # untuk menambahkan baris baru

# contoh tipe data dari bytearray
angka_bytearray = bytearray(12)
print(angka_bytearray)
print(type(angka_bytearray))
print()  # untuk menambahkan baris baru

# contoh tipe data dari memoryview
angka_memoryview = memoryview(bytes(12))
print(angka_memoryview)
print(type(angka_memoryview))
