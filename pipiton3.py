# buah = ["mangga", "apel", "pisang", "jeruk", "anggur"]

# print (buah[1 : 4])

# buah = ["mangga", "apel", "pisang", "jeruk", "anggur"]
# print (buah)
# buah.insert(2, "kiwi")


# print (buah)
# buah.remove ("pisang")
# print (buah)

# print (buah)
# del buah[1]
# print (buah)

# print (buah)
# terhapus = buah.pop(2)
# print (buah)
# print ("buah yang terhapus adalah : ", terhapus)

# print (buah)
# buah [2] = "kiwi"
# print (buah)

# Menu = [["nasi goreng", "mie goreng"], ["sate ayam", "sate kambing", "sate sapi"]]
# print (Menu[0][1])


# buah = ["mangga", "apel", "pisang", "jeruk", "anggur"]  
# cari_buah   = input("Masukkan nama buah yang ingin dicari : ")
# if cari_buah in buah:
#     print ("buah ada di dalam list")
# else:
#     print ("buah tidak ditemukan")

# jadwal_matkul = ["dasar dasar pemograman", "pengantar teknologi informasi", "matematika diskrit", "bahasa inggris" ]
# print(jadwal_matkul)
# print ("jadwal bentrok, jadi")
# # jadwal_matkul.insert(1, "agama islam")
# # jadwal_matkul.insert(2, "pkn")
# jadwal_matkul.remove(jadwal_matkul.index("dasar dasar pemograman"))
# jadwal_matkul.remove(jadwal_matkul.index("pengantar teknologi informasi"))
# jadwal_matkul.insert(jadwal_matkul.index("pkn"), "agama islam")
# for i in range (len(jadwal_matkul)):
#     print (jadwal_matkul[i])


#     hapus = input(Nama + ", mau hapus data siapa ya? : ")
# if hapus == "ya":
#     nama_hapus = input("Masukkan nama mahasiswa yang ingin dihapus : ")
#     for data in mahasiswa:
#         if data[0].lower() == nama_hapus.lower():
#             mahasiswa.remove(data)
#         if data in lulus:
#             lulus.remove(data)
#         if data in remedi:
#             remedi.remove(data)
#     print ("Data mahasiswa berhasil dihapus")
# else:
#     print ("Data mahasiswa tidak dihapus")

hapus = input(Nama + ", kamu mau hapus data atau enggak? (ya/tidak) : ")
if hapus.lower() == "ya":
    nama_hapus = input(Nama + ", mau hapus data siapa ya? : ")
    ditemukan = False

    for data in mahasiswa:
        if data[0].lower() == nama_hapus.lower():
            ditemukan = True
            mahasiswa.remove(data)
            if data in lulus:
                lulus.remove(data)
            if data in remedi:
                remedi.remove(data)
            print ("Data mahasiswa berhasil dihapus")
            break

    if ditemukan == False:
        print ("Data mahasiswa tidak ditemukan")
elif hapus.lower() == "tidak":
    print ("Oke, data mahasiswa tidak dihapus")
else :
    print ("pilihan tidak valid.")
