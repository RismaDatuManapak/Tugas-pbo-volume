class Luas:
    def __init__(self):
        self.satu = angka1
        self.dua = angka2
    def persegi_panjang(self,):
        print(self.satu * self.dua)
    def lingkaran(self):
        print(self.satu * self.dua * self.dua)
    def segitiga(self):
        print(1/2 * (self.satu * self.dua))

class Volume:
    def __init__(self):
        self.satu = angka1
        self.dua = angka2
        self.tiga = angka3
    def kubus(self):
        print(self.satu**3)
    def balok(self):
        print(self.satu*self.dua*self.tiga)
    def bola(self):
        print(self.satu*self.dua*(self.tiga**3))
    def tabung(self):
        print(self.satu*(self.dua**2)*self.tiga)
    def kerucut(self):
        print(1/3*(self.satu*(self.dua**2)*self.tiga))


print( "Hitung Luas & Volume".center(46))
while True:
    print("\n1. hitung Luas \n2. hitung Volume \n3. Keluar")
    pilihan = int(input("Masukkan Pilihan : "))
    if pilihan == 1:
            print("\n1. Persegi / Persegi Panjang \n2. Lingkaran \n3. Segitiga \n4. Kembali")
            pilihan = int(input("Masukkan Pilihan : "))
            if pilihan == 1:
                angka1 = float(input("Masukkan panjang persegi : "))
                angka2 = float(input("Masukkan lebar persegi : "))
                hasil = Luas()
                hasil.persegi_panjang()
                print("masih ingin lanjut?")
                print("-ya- untuk lanjut & -Tidak- untuk break")
                tnya = input(": ")
                if tnya == "ya" :
                    print(pilihan)
                else:
                    break             
            elif pilihan == 2:
                angka1 = 3.14
                angka2 = float(input("Masukkan Jari-Jari Lingkaran : "))
                hasil = Luas()
                hasil.lingkaran()
                print("masih ingin lanjut?")
                print("-ya- untuk lanjut & -Tidak- untuk break")
                tnya = input(": ")
                if tnya == "ya" :
                    print(pilihan)
                else:
                    break            
            elif pilihan == 3:
                angka1 = float(input("Masukkan Tinggi Segitiga : "))
                angka2 = float(input("Masukkan Alas Segitiga : "))
                hasil = Luas()
                hasil.segitiga()
                print("masih ingin lanjut?")
                print("-ya- untuk lanjut & -Tidak- untuk break")
                tnya = input(": ")
                if tnya == "ya" :
                    print(pilihan)
                else:
                    break            
            elif pilihan == 4:
                break
            else:
                print("Perintah Tidak Ditemukan")
    elif pilihan == 2:
            print("\n1. Kubus \n2. Bola \n3. Tabung \n4. Kerucut \n5. Kembali")
            pilihan = int(input("Masukkan Pilihan : "))
            if pilihan == 1:
                angka1 = float(input("Masukkan panjang rusuk : "))
                angka2 = 0
                angka3 = 0
                hasil = Volume()
                hasil.kubus()
                print("masih ingin lanjut?")
                print("-ya- untuk lanjut & -Tidak- untuk break")
                tnya = input(": ")
                if tnya == "ya" :
                    print(pilihan)
                else:
                    break            
            
            elif pilihan == 2:
                angka1 = 4/3
                angka2 = 3.14
                angka3 = float(input("Masukkan Jari-Jari Bola : "))
                hasil = Volume()
                hasil.bola()
                print("masih ingin lanjut?")
                print("-ya- untuk lanjut & -Tidak- untuk break")
                tnya = input(": ")
                if tnya == "ya" :
                    print(pilihan)
                else:
                    break            
            elif pilihan == 3:
                angka1 = 3.14
                angka2 = float(input("Masukkan Jari-Jari Lingkaran : "))
                angka3 = float(input("Masukkan Tinggi Tabung : "))
                hasil = Volume()
                hasil.tabung()
                print("masih ingin lanjut?")
                print("-ya- untuk lanjut & -Tidak- untuk break")
                tnya = input(": ")
                if tnya == "ya" :
                    print(pilihan)
                else:
                    break            
            elif pilihan == 4:
                angka1 = 3.14
                angka2 = float(input("Masukkan Jari-Jari Lingkaran : "))
                angka3 = float(input("Masukkan Tinggi Kerucut : "))
                hasil = Volume()
                hasil.kerucut()
                print("masih ingin lanjut?")
                print("-ya- untuk lanjut & -Tidak- untuk break")
                tnya = input(": ")
                if tnya == "ya" :
                    print(pilihan)
                else:
                    break            
            elif pilihan == 5:
                break
            else:
                print("Perintah Tidak Ditemukan")

    elif pilihan == 3:
        break
    else:
        print("Perintah Tidak Ditemukan")