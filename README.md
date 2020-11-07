# labspy02

# DAFTAR TUGAS

<table border="2" cellpading="10">
  <tr>
    <td><b>Pertemuan 7</b></td>
    <td>Lab3</td>
    <td><a href="https://github.com/Wayisalqorni/pratikum-python.git">Klik disini</td>
  </tr>

</table>

# TUGAS PPT 2

## SOAL

![soal](foto/soal.PNG)

## JAWABAN
  - Buka text editor, seperti PyCharm, Visual Studio, Atom, dan lain-lain.
  - Kemudian salin kode berikut ini


        1   #program menampilkan angka terbesar dari 3 inputan
        2
        3   a = int(input("Masukkan nilai a: "))
        4   b = int(input("Masukkan nilai b: "))
        5   c = int(input("Masukkan nilai c: "))
        6
        7   if(a > b) and (a > c):
        8       print('Nilai a paling besar, yaitu', a)
        9   elif(b > a) and (b > c):
        10      print('Nilai b paling besar, yaitu', b)
        11  else:
        12      print('Nilai c paling besar, yaitu', c)
        13

![ppt1](foto/ppt1.PNG)

  - Simpan dengan nama `labspy02.py`, Kemudian jalankan program tersebut. Maka akan menampilkan output sebagai berikut

![ppt2](foto/ppt2.PNG)

  - Flowchart dari program tersebut

  ![flowchart](foto/flowchart.PNG)

## PENJELASAN
  - Pada baris ke-3, menginstruksikan kita untuk memasukkan nilai **a**, kemudian akan disimpan dalam variabel `a` dalam bentuk integer.

  - Pada baris ke-4, menginstruksikan kita untuk memasukkan nilai **b**, kemudian akan disimpan dalam variabel `b` dalam bentuk integer.

  - Pada baris ke-5, menginstruksikan kita untuk memasukkan nilai **c**, kemudian akan disimpan dalam variabel `c` dalam bentuk integer.

  - Di baris ke-7, ada klausa `if` untuk pilihan kondisi pertama, dan `and` merupakan operasi logika, hasilnya adalah _True_ jika kedua operatornya bernilai benar. Misalnya

    - `a=4`,`b=10`,`c=5`, _"Jika nilai `a` lebih besar dari `b`"_ **(ini benar)**, dan _"Jika nilai `a` lebih besar dari `c`"_ **(ini benar)**. Maka program berlanjut ke baris-8, _cetak nilai `a` ke layar_.


  ![ppt2](foto/ppt2.PNG)