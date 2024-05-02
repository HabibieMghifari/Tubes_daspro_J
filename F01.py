import csv

def load_data(filename):
    list = []
    with open(filename) as csv_file:
        data = csv.reader(csv_file, delimiter = ';')
        next(data) #skip header
        for row in data:
            list.append(row)
        return list
    
def atribut(data, a): # mengambil data pada 1 baris
    variabel = []
    for row in data:
        variabel.append(row[a])
    return variabel

# contoh penggunaan
# username = atribut(data, 1)
# print(username)

def validate_username(username):
    valid_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
    for char in username:
        if char not in valid_chars:
            return False
    return True

# Program F01 - REGISTER
data = load_data('user.csv')
monster = load_data('monster.csv')

id = atribut(data, 0)
username = atribut(data, 1)
password = atribut(data, 2)
role = atribut(data, 3)
oc = atribut(data, 4)

print('REGISTER')
user = input("Masukkan username: ")
password = input("Masukkan password: ")

for i in range(len(id)):
    if (user==username[i]):
        print(f"Username {user} sudah terpakai, silahkan gunakan username lain!")
        break
    else:
        if (validate_username(user)!=True):
            print("Username hanya boleh berisi alfabet, angka, underscore, dan strip!")
            break
        else:
            type = atribut(monster, 1)
            print("Silahkan pilih salah satu monster sebagai monster awalmu.")
            for i in range(len(type)):
                print(f"{i+1}. {type[i]}")
            a = int(input("Monster pilihanmu: "))
            print(f"Selamat datang Agent {user}. Mari kita mengalahkan Dr. Asep Spakbor dengan {type[a-1]}!")
            break


            



