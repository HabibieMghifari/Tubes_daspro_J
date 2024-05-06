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
#from F01 import 
username = load_data('user.csv', 1)
password = load_data('user.csv', 2)
print("Login")
#def login(user,password):
status = False
loginu=[]
def login_system(x, y, username, password, status, loginu):
    for i in range (len(username)) :
        if x==username[i] and y==password[i] and status != True:
            status=True
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
        
 #   return (user,password)
#login(x,y)
x=input("Username : ")
y=input("Password : ")
login_system(x, y, username, password, status, loginu)
