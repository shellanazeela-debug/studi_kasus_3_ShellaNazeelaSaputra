# studi_kasus_3_ShellaNazeelaSaputra

Nama: Shella Nazeela Saputra<br>
NIM: 2609116018

<br>
<img width="210" height="32" alt="Screenshot 2026-09-08 204610" src="https://github.com/user-attachments/assets/d98de33e-d806-4cc2-a4d7-b26ba72c4888" /> <br>
1. Fungsi diatas berfungsi untuk membuat sebuah Tuple bernama batas_nilai. isi Tuple diatas memiliki batas minimal nilai lulus 65 dan batas maksimal nilai 100 <br>
<br>
<img width="157" height="57" alt="Screenshot 2026-09-08 205106" src="https://github.com/user-attachments/assets/a2a12b57-7434-4196-ab74-041fa25e5969" /> <br>
2. Fungsi diatas digunakan untuk membuat List kosong bernama mahasiswa. List ini nantinya digunakan untuk menyimpan semua data mahasiswa. Selain itu, untuk fungsi lulus digunakan untuk menyimpan data mahasiswa yang mendapat nilai lulus. Dan untuk fungsi remedi, digunakan untuk menyimpan data mahasiswa yang mendapat nilai remedi. <br>

<img width="503" height="49" alt="Screenshot 2026-09-08 205515" src="https://github.com/user-attachments/assets/40ab3cb2-b0fc-4f91-b0d5-33ab141ed3e8" /> <br>
3. untuk baris ke-8 berfungsi untuk menampilkan batas minimal nilai lulus. batas_nilai[0] mengambil isi Tuple pada indeks ke-0.Selain itu, untuk baris ke-9 berfungsi untuk menampilkan batas maksimal nilai lulus. Dan terakhir, baris ke-10 berfungsi untuk meminta pengguna memasukkan nama. Input() digunakan untuk menerima data dari pengguna.<br>

<img width="459" height="114" alt="Screenshot 2026-09-08 210613" src="https://github.com/user-attachments/assets/d1352412-1a4d-4976-8441-12c95e44ac72" /> <br>
4.Bagian ini digunakan untuk memasukkan data mahasiswa ke dalam program. Pertama, user diminta menentukan jumlah mahasiswa yang akan dimasukkan. Fungsi int() digunakan agar jumlah yang dimasukkan dapat diproses sebagai bilangan bulat.Setelah itu, perulangan for digunakan agar proses input nama dan nilai dilakukan sesuai dengan jumlah mahasiswa yang telah ditentukan. Setiap mahasiswa memiliki dua data, yaitu nama dan nilai, yang digabungkan ke dalam List data_mahasiswa. Data tersebut kemudian dimasukkan ke dalam List mahasiswa menggunakan fungsi append().<br>

<img width="411" height="58" alt="Screenshot 2026-09-08 210623" src="https://github.com/user-attachments/assets/3b311cba-4b08-4070-91a3-e7a9b27c3990" /> <br>
5.Bagian ini digunakan untuk mengetahui dan menentukan akan status mahasiswa berdasarkan nilai yang telah dimasukkan. Percabangan if memeriksa apakah nilai mahasiswa lebih besar atau sama dengan batas minimal 65 dan tidak melebihi batas maksimal 100. Operator and digunakan agar kedua kondisi tersebut harus terpenuhi. ketika suatu kondisi terpenuhi, data mahasiswa dimasukkan ke List lulus.Namun, jika nilai tidak memenuhi kondisi tersebut, data mahasiswa dimasukkan ke List remedi.<br>

<img width="321" height="206" alt="Screenshot 2026-09-08 210646" src="https://github.com/user-attachments/assets/43a04595-b32b-4789-885d-7fc45fd03635" /> <br>
6. Bagian ini digunakan untuk menampilkan data yang dimasukkan dan dikelompokkan oleh program. Perulangan for digunakan untuk mengambil setiap data yang terdapat dalam List. Program menampilkan tiga kelompok data, yaitu seluruh mahasiswa, mahasiswa yang lulus, dan mahasiswa yang harus remedi. Yang dimana berdasar data diatas, setiap mahasiswa dikelompokkan sesuai dengan perolehan nilainya. <br>

<img width="386" height="88" alt="Screenshot 2026-09-08 210712" src="https://github.com/user-attachments/assets/8546866a-6751-4401-a400-49c57ee5b7fb" /> <br>
7.Bagian ini digunakan untuk memberikan pilihan kepada pengguna saat seluruh data mahasiswa sudah ditampilkan semuanya. Terdapat tiga pilihan yang dapat digunakan, yaitu tidak melakukan perubahan, mengedit nilai mahasiswa, atau menghapus data mahasiswa. Pilihan pengguna disimpan dalam variabel pilihan. Data tersebut kemudian digunakan oleh percabangan if dan elif untuk menentukan tindakan yang akan dijalankan oleh program. <br>

 <img width="426" height="47" alt="Screenshot 2026-09-08 210826" src="https://github.com/user-attachments/assets/679b9149-f0a4-469a-9bf8-c71c9f61c0be" /> <br>
8. Fungsi berikut merupakan isi dari pilihan pertama yang memaksudkan user untuk tidak melakukan sebuah perubahan. Program akan melewati proses edit maupun hapus dan mempertahankan seluruh data seperti sebelumnya. Pesan "tidak ada data yang diubah" ditampilkan untuk memberikan informasi kepada pengguna bahwa tidak terjadi perubahan pada data mahasiswa. <br>

<img width="593" height="398" alt="Screenshot 2026-09-08 210847" src="https://github.com/user-attachments/assets/b84f3ba0-7a99-45c1-83ab-1aaf59f80151" /> <br>
9.Fungsi ini berfungsi untuk mengubah nilai mahasiswa yang sebelumnya sudah dimasukkan ke dalam program. Pertama,user diminta untuk memasukkan nama mahasiswa yang ingin diubah nilainya. Setelah itu, program menggunakan perulangan for untuk mencari nama tersebut di dalam List mahasiswa . Penggunaan .lower()  bertujuan supaya pencarian nama tetap bisa dilakukan meskipun pengguna menulisnya dengan huruf besar atau huruf kecil. Adapun, terdapat variabel `ditemukan` yang digunakan untuk mengetahui apakah nama mahasiswa yang dicari ada di dalam data. Jika nama mahasiswa ditemukan, program akan menampilkan nilai sebelumnya dan meminta pengguna untuk memasukkan nilai yang baru. Nilai tersebut kemudian dicek terlebih dahulu agar tidak kurang dari 0 atau lebih dari 100. Jika nilai baru sudah sesuai, program akan mengganti nilai lama dengan nilai yang baru. Data mahasiswa tersebut juga dihapus terlebih dahulu dari List yang ada seperti lulus dan juga remedi agar data sebelumnya tidak tetap tersimpan dan menyebabkan hasil yang salah. Setelah itu, program akan mengecek kembali nilai terbaru untuk menentukan apakah mahasiswa tersebut masuk ke kategori lulus atau remedi. Perintah `break` digunakan untuk menghentikan perulangan. <br>

<img width="582" height="344" alt="Screenshot 2026-09-08 210909" src="https://github.com/user-attachments/assets/2b932d76-5765-4f44-ab94-dd4fe41d120e" /> <br>
10.Fungsi ini digunakan untuk menghapus data mahasiswa yang sudah ada di dalam program. Pertama, pengguna diminta untuk memasukkan nama mahasiswa yang ingin dihapus. Setelah itu, program akan mencari nama tersebut menggunakan perulangan for dan kondisi if. Kalau nama mahasiswa ditemukan, program akan menampilkan nama dan nilai mahasiswa tersebut sebelum data dihapus. Sebelum data benar-benar dihapus, program akan meminta konfirmasi terlebih dahulu kepada pengguna. Jika pengguna menjawab "ya", maka data mahasiswa akan dihapus menggunakan fungsi remove(). Data tersebut juga akan dihapus dari List lulus atau remedi jika sebelumnya masuk ke salah satu List tersebut. Kalau pengguna menjawab "tidak", maka data tidak akan dihapus dan tetap tersimpan di dalam program. Variabel ditemukan digunakan untuk menandai apakah nama mahasiswa yang dicari ada di dalam data atau tidak. <br>

<img width="545" height="79" alt="Screenshot 2026-09-08 210918" src="https://github.com/user-attachments/assets/2abdbd05-ba5c-47d6-8a27-73495e767fa4" /> <br>.
11.Fungsi terakhir digunakan untuk menampilkan hasil data mahasiswa setelah sebelumnya dilakukan proses edit atau hapus data. Pada bagian ini, program akan menampilkan semua data mahasiswa yang masih tersimpan, kemudian menampilkan juga mahasiswa yang masuk ke dalam kategori lulus dan remedi. Dengan begitu, pengguna bisa melihat apakah perubahan yang dilakukan sebelumnya sudah sesuai atau belum. Setelah semua data selesai ditampilkan, program akan memberikan pesan penutup dengan mencantumkan nama pengguna yang sudah dimasukkan di awal program. Pesan tersebut menandakan bahwa seluruh proses sudah selesai dan program telah selesai digunakan.<br>







