# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 08:55:30 2021

@author: Tio Chalil Gibran Findianto | 20083000152 - 2E
"""

"Quiz 2 Sebelumnya UAS"
"-------------------------------------------------------------------------------------------------------"
#Bu Sung Hin seorang pemilik bengkel motor UD. Matahari memesan sebuah program kepada Anda untuk dapat 
#menampilkan beberapa merek Oli motor yang ada pada komputer. Sehingga konsumen dapat memilih dan 
#membeli oli dalam jumlah yang diinginkannya dan mengetahui jumlah uang yang harus dibayarnya. 
#Berikut daftar merk oli motor yang dijualnya:
#a. Duration SW20 1L @ Rp53.000
#b. Castrol Magnatec 1L @ Rp50.000
#c. Federal Supreme XX 1L @ Rp54.000
#d. Yamalube 1L @ Rp45.000
#e. Shell 1L @ Rp46.000
#Pembeli akan diberikan potongan 5% bila total pembelian sebelum PPN bernilai minimal Rp 200.000.
#Dari seluruh total pembayaran tersebut akan dikenakan pajak PPN 1%

jwbulangbelilagi ="y"
#nilai default jawab
while jwbulangbelilagi=="y" or jwbulangbelilagi=="Y":
    
    print("==================================================================")
    print("            TRANSAKSI PERBAIKAN DI BENGKEL MOTOR UD")
    print("==================================================================")
    print(" Kode = A. Duration SW20 1L")
    print(" Kode = B. Castrol Magnatec 1L")
    print(" Kode = C. Federal Supreme XX 1L")
    print(" Kode = D. Yamalube 1L")
    print(" Kode = E. Shell 1L")
    print("------------------------------------------------------------------")
    
    kode = ['a','b','c','d','e']
    merk = ['Duration SW20','Castrol Magnatec 1L','Federal Supreme XX 1L','Yamalube 1L','Shell 1L']
    harga = [53000,50000,54000,45000,46000]
    diskon = [5]
    ppn = [1]
    
    pilihan = input("--> Masukkan Kode Merk         = ")
    
    #identifikasi pilihan
    if pilihan=="a":
        idx = 0
    elif pilihan=="b":
        idx = 1
    elif pilihan=="c":
        idx = 2
    elif pilihan=="d":
        idx = 3
    elif pilihan=="e":
        idx = 4
    else:
        idx = 0
    
    #Cek tampilkan layar
    print("--> Pilihan Merk               = " + merk[idx])
    print("--> Pilihan Harga Barang       = Rp." + str(harga[idx]))
    print("--> Dapatkan Nilai Diskon      = " + str(diskon[idx]) + " %")
    print("--> Kena PPN                   = " + str(ppn[idx]) + " %")
    
    #Hitung Transaksi
    fixmerk = merk[idx]
    fixharga = harga[idx]
    fixdiskon = diskon[idx]
    fixppn = ppn[idx]
    totbiaya = fixharga / fixdiskon
    
    #Total Biaya
    print("--> Total Biaya                = Rp." + str(totbiaya))

    #Inputan jawaban dari user
    jwbulangbelilagi = input("--> Mau Beli Lagi? y/t = ")
    if jwbulangbelilagi=="t" or jwbulangbelilagi=="T":
            break
        