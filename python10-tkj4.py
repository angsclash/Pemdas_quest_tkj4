# membuat tipe data list

koleksi_data_str = ["pisang","mangga","pepaya","semangka"]

koleksi_data_int = [200, 300, 400, 500]

koleksi_data_mix = ["nasir", 100, True, "fuad"]

print("koleksi data string:",koleksi_data_str)

print("koleksi data integer:",koleksi_data_int)

print("koleksi data mix:",koleksi_data_mix)

# buatlah 3 kumpulan data : nama hewan, nilai uts, teman sebangku

nama_hewan = ["monyed", "domge", "icikiwir", "blue lobster"]
nilai_uts = [100, 85, 70, 99, 20]
nama_teman_wibu = ["fajeri python", "ripeki cefot", "ilal imreng", "rafi baskath"]

print("nama nama hewan yang kemce:",nama_hewan)
print("nilai nilai uts yang gegeh:",nilai_uts)
print("nama temen temen gweh yang wibuh pencoly handal:",nama_teman_wibu)


# data ke 2 nama hewan

print("nama hewan data ke-2:", nama_hewan[1])

# data pertama nilai uts

print("data pertama nilai uts:", nilai_uts[0])

# data terakhir nama teman sebangku

print("data terakhir nama teman sebangku:", nama_teman_wibu[3])


# tambahkan 1 data disetiap data koleksi

nama_hewan.append("semut")
nilai_uts.append(55)
nama_teman_wibu.append("selamet")
print(nama_hewan, nilai_uts, nama_teman_wibu)
# ubahlah data terakhir nilai uts

nilai_uts[-1] = 69
print(nilai_uts)
# ubahlah data ke-3 nama hewan

nama_hewan[-2] = "burung"
print(nama_hewan)
