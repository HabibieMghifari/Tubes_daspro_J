#khusus admin
import os

def load_data(data, x):
    list = []
    with open(data, 'r') as file:
        # Lewati header
        file.readline()
        nilai = ''
        kolom = 0
        for line in file:
            for char in line:
                if char == ';':  # akhir nilai
                    if kolom == x:
                        list.append(nilai)
                    nilai = ''
                    kolom += 1
                elif char == '\n':  # akhir baris
                    if kolom == x:
                        list.append(nilai)
                    nilai = ''
                    kolom = 0
                else:
                    nilai += char
    return list

def monster_adder(filename, type, atk_power, def_power, hp):
    # Tentukan role dan oc
    #role = 'agent'
    #oc = 0

    # Periksa apakah file csv ada dan tentukan ID berikutnya
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1]
                next_id = int(last_line.split(';')[0]) + 1
            else:
                next_id = 2
    else:
        next_id = 2
    with open(filename, 'a') as file:
        file.write(f"{next_id};{type};{atk_power};{def_power};{hp}\n")

def monster_management(z):
    while z<4:
        z=int(input(f"Masukkan Pilihan Anda!\n"))
        if z == 1 :
            monster_name=load_data('monster.csv',1)
            monster_atk=load_data('monster.csv',2)
            monster_def=load_data('monster.csv',3)
            monster_hp=load_data('monster.csv',4)
            print(f"{monster_name}\n{monster_atk}\n{monster_def}\n{monster_hp}")
        elif z==2:
            l=input("Nama Monster : ")
            m=int(input("atk_power : "))
            n= int(input("def_power : "))
            o= int(input("hp : "))
            p=input(f"apakah yakin dengan penambahan monster ini? ketik Y/N\n")
            if p=="Y" :
                monster_adder('monster.csv',l,m,n,o)
                print("Monster berhasil ditambahkan!")
            elif p=="N" :
                print("Monster gagal ditambahkan!")
        elif z==3:
            print("Selamat tinggal!")
            break
from F02 import admin #nanti klo udh disatuin gausah pake import admin, langsung aja if admin==true (abis dipilih dari menu ya btw)
z=0
if admin == True :
    print("Selamat Datang Pada Monster management!\n1. Tampilkan Semua Monster\n2. Tambah Monster\n3. Keluar")
    monster_management(z)
else :
    print("Maaf fungsi ini khusus admin!")



