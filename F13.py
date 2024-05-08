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


from F02 import status
from F02 import admin
if admin == True :
    monster_name=load_data('monster.csv',1)
    print(monster_name)
#load_data('monster.csv',)

