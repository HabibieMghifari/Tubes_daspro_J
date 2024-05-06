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

# Program F01 - REGISTER
id = load_data('user.csv', 0)
username = load_data('user.csv', 1)
print(username)

print('REGISTER')
user = input("Masukkan username: ")
password = input("Masukkan password: ")

logout_status = False
for i in range(len(id)):
    if (user==username[i]):
        print(f"Username {user} sudah terpakai, silahkan gunakan username lain!")
        break
    elif (logout_status == True):
        print(f"Register gagal!\nAnda telah login dengan username {user}, silahkan lakukan 'LOGOUT' sebelum melakukan register.")
        break
    else:
        if (validate_username(user)!=True):
            print("Username hanya boleh berisi alfabet, angka, underscore, dan strip!")
            break
        elif (user!=username[i]) and (logout_status == True):
            csvwriter('user.csv', user, password)
            type = load_data('monster.csv', 1)
            print("Silahkan pilih salah satu monster sebagai monster awalmu.")
            for i in range(len(type)):
                print(f"{i+1}. {type[i]}")
            a = int(input("Monster pilihanmu: "))
            print(f"Selamat datang Agent {user}. Mari kita mengalahkan Dr. Asep Spakbor dengan {type[a-1]}!")
            break
