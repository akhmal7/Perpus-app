buku=[]
def tampil():
  index=0
  if len(buku)<=0:
    print("data masih kosong")
  else :
    for book in buku:
      print(str(index)+" "+(book))
      index=index+1

def tambah():
  judul=input("masukkanjudul buku ")
  buku.append(judul)
  print("buku baru telah ditambahkan")
def edit():
  tambah()
  index=int(input("masukkan index: "))
  judul_lama=buku[index]
  judul_baru=input("masukkan judul baru :")
  buku[index]=judul_baru
  print(judul_lama+"telah diganti ke "+judul_baru)
def hapus():
  tampil()
  index=int(input("masukkan index: "))
  judul=buku[index]
  del buku[index]
  print(judul+"telah di hapus")
def menu():
  print("1 | Tampilkan Data")
  print("2 | Tambahkan Data")
  print("3 | Edit Data")
  print("4 | Hapus Data")

  kode = input("masukkan pilihan :")
  if kode == "1":
    tampil()
  elif kode =="2":
    tambah()
  elif kode =="3":
    edit()
  elif kode == "4":
    hapus()
  else :
    print("kode salah")

while(True):
  menu()