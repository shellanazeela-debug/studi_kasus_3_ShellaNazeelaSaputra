batas_nilai = (65,100)

#list 
mahasiswa = []
lulus = []
remedi = []

print ("Nilai minimal untuk lulus adalah : ", batas_nilai[0])
print ("Nilai maksimal untuk lulus adalah : ", batas_nilai[1])
Nama = input ("sebelum mengakses program ini, silahkan masukkan nama anda : ")

jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa : "))
for i in range (jumlah_mahasiswa):
    print ("data mahasiswa ke-", i + 1)
    nama = input("Masukkan nama mahasiswa : ")
    nilai = int(input("Masukkan nilai mahasiswa : "))
    data_mahasiswa = [nama, nilai]
    mahasiswa.append(data_mahasiswa)

    if nilai >= batas_nilai[0] and nilai <= batas_nilai[1]:
        lulus.append(data_mahasiswa)
    else:
        remedi.append(data_mahasiswa)

print ("==SEMUA DATA MAHASISWA==")
for data in mahasiswa:
    print ("nama : ", data[0])
    print ("nilai : ", data[1])

print ("==DATA MAHASISWA LULUS==")
for data in lulus:
    print ("nama : ", data[0])
    print ("nilai : ", data[1])

print ("==DATA MAHASISWA REMEDI==")
for data in remedi:
    print ("nama : ", data[0])
    print ("nilai : ", data[1])

print("silahkan dipilih ya", Nama, "mau opsi yang mana?")
print ("1. Tidak melakukan perubahan")
print ("2. Edit nilai mahasiswa")
print ("3. Hapus data mahasiswa")

pilihan = input("pilih menu (1/2/3) ya " + Nama + "!")
if pilihan == "1":
    print ("tidak ada data yang diubah.")

elif pilihan == "2":
    nama_edit = input("masukkan nama yang akan anda edit :")
    ditemukan = False
    for data in mahasiswa:
        if data[0].lower() == nama_edit.lower():
            ditemukan = True
            print("Data mahasiswa ditemukan")
            print("nama : ", data[0])
            print("nilai : ", data[1])
            nilai_baru = int(input("Masukkan nilai baru mahasiswa : "))
            if 0 <= nilai_baru <= batas_nilai[1]:
                data_baru = [data[0], nilai_baru]
                mahasiswa[mahasiswa.index(data)] = data_baru
                if data in lulus:
                    lulus.remove(data)
                if data in remedi:
                    remedi.remove(data)
                if nilai_baru >= batas_nilai[0]:
                    lulus.append(data_baru)
                else:
                    remedi.append(data_baru)
                print("nilai berhasil diperbarui")
            else:
                print("nilai harus berada di antara 0-100")
            break
    if not ditemukan:
        print("Data mahasiswa tidak ditemukan")
                

    
elif pilihan == "3":
    nama_hapus = input("masukkan nama yang akan anda hapus :")
    ditemukan = False
    for data in mahasiswa:
        if data[0].lower() == nama_hapus.lower():
            print ("data yang akan dihapus:")
            print("nama :", data[0])
            print("nilai :", data[1])

            konfirmasi = input ("yakin ingin menghapus? (ya/tidak) :").lower()
            if konfirmasi == "ya" :
                
                mahasiswa.remove(data)
                if data in lulus:
                    lulus.remove(data)
                if data in remedi:
                    remedi.remove(data)
                print("Data mahasiswa berhasil dihapus")
            else :
                print ("data tidak jadi dihapus")
                ditemukan = True
                break
    if not ditemukan:
        print("Data mahasiswa tidak ditemukan")
        

print ("==SEMUA DATA MAHASISWA==")
print ("semua data mahasiswa : ", mahasiswa)
print ("data mahasiswa lulus : ", lulus)
print ("data mahasiswa remedi : ", remedi)
print ("Terimakasih " , Nama ," sudah menggunakan program ini, semoga bermanfaat!")
