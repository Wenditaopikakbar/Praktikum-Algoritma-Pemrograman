print("=========TOKO SEMBAKO========")
NamaPembeli = input("Nama Pembeli : ")
Alamat      = input("Alamat       : ")
NoTelp      = input("No.Telp      : ")
Tanggal     = input("Tanggal      : ")

print(" ========================================")
print(" -----Selamat Datang di Toko Sembako-----")
print(" ---------List Menu Toko Sembako---------") 
print(" ========================================")
print(" 1. Telur            : Rp.2500")
print(" 2. Mie Goreng       : Rp.3000")
print(" 3. Mie Goreng Isi 2 : Rp.4000")
print(" 4. Roti             : Rp.2000")
print(" 5. Aqua             : Rp.5000")
print(" ========================================")
listBarang=str(input(" Masukkan angka sesuai dengan barang yang tersedia = "))
jumlahPesanan=int(input(" Jumlah dibeli = "))
if listBarang == "1":
    namaBarang= "Telur"
    harga = "2500"
    totalHarga=(2500*jumlahPesanan)
    if jumlahPesanan >= 1000:
        totalHarga=(2500*jumlahPesanan)
    else :
        totalHarga=int(totalHarga)
elif listBarang == "2":
    namaBarang= "Mie Goreng"
    harga = "3000"
    totalHarga = (3000*jumlahPesanan)
    if jumlahPesanan >= 1000:
        totalHarga=(3000*jumlahPesanan)
    else :
        totalHarga=int(totalHarga)
elif listBarang == "3":
    namaBarang= "Mie Goreng Isi 2"
    harga = "4000"
    totalHarga= (4000*jumlahPesanan)
    if jumlahPesanan >= 1000:
        totalHarga=(4000*jumlahPesanan)
    else :
        totalHarga=int(totalHarga)
elif listBarang == "4":
    namaBarang= "Roti"
    harga = "2000"
    totalHarga= (2000*jumlahPesanan)
    if jumlahPesanan >= 1000:
        totalHarga=(2000*jumlahPesanan)
    else :
        totalHarga=int(totalHarga)
elif listBarang == "5":
    namaBarang= "Aqua"
    harga ="5000"
    totalHarga=(5000*jumlahPesanan)
    if jumlahPesanan >= 1000:
        totalHarga=(5000*jumlahPesanan)
    else :
        totalHarga=int(totalHarga)
else:
    barang=input(" Maaf,Barang yang dipilih tidak tersedia di Toko")
 
print(" ------------------------------")
print(" ---------TOKO SEMBAKO---------")
print(" ------------------------------")
print(" Nama             :", NamaPembeli)
print(" Alamat           :", Alamat)
print(" No.Telp          :", NoTelp)
print(" Tanggal          :", Tanggal)
print(" Barang           :", namaBarang)
print(" Jumlah Pesanan   :", jumlahPesanan)
print(" Harga            :", harga)
print(" ------------------------------")
print(" Total Pembayaran :", totalHarga)
print(" ------------------------------")