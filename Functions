import os
#dari F01
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

def csvwriter(filename, username, password):
    # Tentukan role dan oc
    role = 'agent'
    oc = 0

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
        file.write(f"{next_id};{username};{password};{role};{oc}\n")

def validate_username(username):
    valid_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
    for char in username:
        if char not in valid_chars:
            return False
    return True
#dari F02
def login_system(x, y, username, password, loginu):
    global status
    global admin
    for i in range (len(username)) :
        if x==username[0] and y==password[i] and status != True:
            status = True
            admin = True
            loginu.append(x)
            print(f"Selamat datang, Agent {x}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.")
            break
        elif x==username[i] and y==password[i] and status != True:
            status = True
            loginu.append(x)
            print(f"Selamat datang, Agent {x}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.")
            break
        elif x!=username[i] and y==password[i] :
            print("Username tidak terdaftar!")
            break
        elif x==username[i] and y!=password[i]:
            print("Password salah!")
            break
        elif status==True :
            print(f"Login gagal!\nAnda telah login dengan username {x}, silahkan lakukan “LOGOUT” sebelum melakukan login kembali.")
            break
#dari F03
def logout(user, password, status):
    if (status == True):
        status = False
        user = ""
        password = ""
        print("Logout berhasil.")
    else :
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    
    return (user, password, status)
#dari F04
#dari F05
#dari F06
#dari F07
#dari F08
#dari F09
#dari F10
#dari F11
#dari F12
#dari F13
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
#dari F14
#dari F15
