# Width and Multiline
# Data
data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44
# string standard
data_string = f"""nama = {data_nama}, umur = {data_umur}, tinggi = 
{data_tinggi}, sepatu = {data_nomor_sepatu}"""
print(5*"="+"Data String"+5*"=")
print(data_string)
# String multiline (dengan menggunakan enter, newline, \n)
data_string = f"""nama = {data_nama},\numur = {data_umur}, \ntinggi = 
{data_tinggi}, \nsepatu = {data_nomor_sepatu}"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)
# String multiline (kutip triplets)
data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)
# mengatur lebar
data_nama = "Ucup Surucup"
data_tinggi = 105.17
data_string = f"""
nama = {data_nama:>5}
umur = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)



# Date and time (latihan)
import datetime as dt
print("Silahkan masukan tanggal, \nbulan dan tahun lahir anda \n")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))
tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")
hari_ini = dt.date.today()
print(f"Hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
print(f"Hari nya adalah : {tanggal_lahir:%A}")
print(f"Umur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan")




# If dan Else Statement
# 1. if nya
# 2. kondisinya
# 3. aksinya
nama = input("Siapa nama anda? ")
# program sebelumnya
# if kondisi: aksi
# program selanjutnya
# 1. program if inline
# if nama=="ucup" : print("Kamu Ganteng abieeez!!!!")
# print(f"Terima kasih {nama}")
# 2. program if indentation
# if nama=="ucup":
# print("kamu ganteng abieeeez!")
# print("kamu juga keren banget!")
# print(f"Terima kasih {nama}")
# 3. Else Statement
if nama=="otong":
    print("hai otooong, si keren!!!")
else:
    print("Ah kamu bukan otong, kamu gak keren! :(")
    print("akhir dari program")