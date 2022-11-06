print ("Authorrized by : Sari Goland")

print ("PROGRAM MENGHITUNG NILAI AKHIR MAHASISWA")

nama=input("Masukkan Nama :")
nim=input("Masukkan nim :")
absensi=input("Masukkan Absensi")
matkul=input("Masukkan Mata Kuliah :")
smtr=input("Masukkan Mata Kuliah :")
tugas=float(input("Masukkan Nilai Tugas :"))
uts=float(input("Masukkan Nilai Uts :"))
uas=float(input("Masukkan Nilai Uas"))

na=(tugas* 0.2) + ( uts * 0.4) + (uas * 0.4)

print("===========HASIL PERHITUNGAN ==========") 

print("Nama : " ,nama)
print("Nim : ",nim)
print("Absensi : ", absensi)
print("Mata kuliah :" ,matkul)
print("Semester : ",smtr)
print("Nilai Tugas : ",tugas)
print("Nilai Uts :" ,uts)
print("Nilai Uas :" ,uas)
