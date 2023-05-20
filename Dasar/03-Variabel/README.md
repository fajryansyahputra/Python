<a href="../02-Tipe-Data">[Tipe Data] ◀ Materi Sebelumnya</a>

<center>

# Variabel
  <p align="center">
  <img src="https://d33wubrfki0l68.cloudfront.net/51b7465eb51f254f7eafb423d312f3c1dc644d00/3d9f2/assets/images/python-variables.svg" width=500 height=250> <br>
  </p">
</center>


<a id="1"><h2>Daftar Isi</h2></a>
  
---

- [Daftar Isi](#1)
- [Pendahuluan](#2)
- [Penempatan Variabel](#3)
- [Penamaan Variabel](#4)
- [Penggunaan Built-in Keyword](#5)
- [Video Penjelasan Tentang Variabel](#6)
- [Praktikum](#7)


<a id="2"><h2>Pendahuluan</h2></a>

---

**Variabel adalah referensi dari sebuah value.** Variabel sering di analogikan seperti **sebuah wadah yang menampung sebuah benda.** Seperti kita ketika ingin menyimpan suatu benda, maka perlu mencari tempat / wadah benda tersebut ingin disimpan terlebih dahulu. Dalam menentukan wadah, kita hanya perlu mencantumkan nama wadah (nama variabel) terlebih dahulu. Setelah itu, python akan secara otomatis mengambilkan wadah sesuai dengan kebutuhan kita. Contoh penggunaan variabel pada Python :

```python
angka_saya = 100
print(angka_saya)

# Outputnya
# 100
```

Pada kode diatas, kita membuat sebuah variabel yang mereferensikan nilai angka `100`. Dengan penggunaan dari variabel kita bisa memanggil lebih dari sekali, misalnya:

```python
angka_saya = 100
print(angka_saya)
print(angka_saya)

# Outputnya
# 100
# 100
```


<a id="3"><h2>Penempatan Variabel</h2></a>

---

Kita bisa menempatkan variabel (_Assign Variable_) dengan variabel lainnya agar mudah untuk mendeklarasikan sebuah nilai yang sama dengan variabel yang berbeda, sebagai contoh:

```python
angka_saya = 100
angka_lain = angka_saya
print(angka_saya)
print(angka_lain)

# Outputnya
# 100
# 100
```

Atau bisa juga dengan cara:

```python
angka_saya = angka_lain = angka_banyak = 100
print(angka_saya)
print(angka_lain)
print(angka_banyak)

# Outputnya
# 100
# 100
# 100
```

Contoh pada string:

```python
nama = nama_alias = "Andi"
print(nama)
print(nama_alias)

# Outputnya
# Andi
# Andi
```


<a id="4"><h2>Penamaan Variabel</h2></a>

---

Python memiliki beberapa peraturan dalam penulisan sebuah variabel. Jika kamu ingin melihat detail aturan tersebut bisa kunjungi laman [PEP8](https://peps.python.org/pep-0008/#type-variable-names) ini. Peraturan tersebut adalah:

1. Menggunakan kata tanpa didahuli dengan angka:

   **Benar** ✅

   ```python
   nama = "Andi"
   ```

   **Salah** ❌

   ```python
   1nama = "Andi"
   ```


2. Menggunakan underscore (garis bawah) jika ingin menggunakan kata yang panjang:

   **Benar** ✅

   ```python
   angka_saya = 11
   ```

   **Salah** ❌

   ```python
   11angka_saya = 11
   ```


3. Variabel pada python bersifat sensitif, penggunaan huruf besar dan kecil sangat diperhatikan:

   contoh

   ```python
   Nama_saya = "Andi" # N kapital
   nama_saya = "Budi" # N kecil
   print(Nama_saya)
   print(nama_saya)

   # Outputnya
   # Andi
   # Budi
   ```

   contoh diatas akan menghasilkan 2 nama karena variabel tersebut secara kalimat sama tapi secara penulisan berbeda, Python memperhatikan hal ini.

Pada Python, penggunaan variabel disarankan menggunakan `snake_case`.


<a id="5"><h2>Penggunaan Built-in Keyword</h2></a>

---

**Built-in keyword** pada Python adalah kata-kata yang mana sudah ditetapkan atau dibuat sebelumnya oleh Python. _Keyword-keyword_ tersebut dibuat untuk melakukan suatu perintah tertentu. Maka dari itu, dalam membuat variabel kita harus menghindari kata-kata tersebut agar program kita tidak terjadi error. Ada beberapa kata yang dilarang untuk digunakan sebagai nama variabel. Contoh penggunaan kata yang dilarang pada Python:

```python
class kelas_saya = "Mipa"
print(kelas_saya)
```

Hasil esekusi diatas akan menyebabkan error karena `class` merupakan salah satu nama fungsi dari Python.


Kata atau _keywords_ yang dilarang:

- False
- None
- True
- and
- as
- assert
- break
- class
- continue
- def
- del
- elif
- else
- except
- finally
- for
- from
- global
- if
- import
- in
- is
- lambda
- nonlocal
- not
- or
- pass
- raise
- try
- return
- while
- with
- yield


<a id="6"><h2>Video Penjelasan Tentang Variabel</h2></a>

---

<center>
  Coming Soon...
</center>

<a id="7"><h2>Praktikum</h2></a>

---

Klik link ini untuk mencoba kode python dari pembahasan kali ini. [Sumber Kode](../03-Variabel/variable.py)

<a href="../04-Operator"> Materi Selanjutnya ▶ [Operator]</a>
