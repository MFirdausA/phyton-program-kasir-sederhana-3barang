print("====PROGRAM KASIR SEDERHANA====")

barang1=input("barang1:")
harga1=int(input("harga:"))
barang2=input("barang2:")
harga2=int(input("harga:"))
barang3=input("barang3:")
harga3=int(input("harga:"))
print()

total=harga1+harga2+harga3
total1=total-(total*20/100)

print()
print("pelanggan membeli:")
print("1.",barang1,"RP.",harga1,"\n"
      "2.",barang2,"RP.",harga2,"\n"
      "3.",barang3,"RP.",harga3,"\n")
print("==================================================")
print(f"total: {total}")
print("==================================================")
print("dapat diskon 20%!")
print("total yang harus dibayar pelanggan: ","Rp.",total1)
print()
uang=int(input("uang pelanggan : "))
print("kembalian","Rp.",uang-total1 )
print()
print("TERIMAKASIH TELAH BERLANJA DI SINI")
