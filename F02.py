from F01 import user
from F01 import password
print("Login")
#def login(user,password):
status = False
loginu=[]
def login_system(x, y, user, password, status, loginu):
    for i in range (len(user)) :
        if x==user[i] and y==password[i] and status != True:
            status=True
            loginu.append(x)
            print(f"Selamat datang, Agent {x}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.")
            break
        elif x!=user[i] and y==password[i] :
            print("Username tidak terdaftar!")
            break
        elif x==user[i] and y!=password[i]:
            print("Password salah!")
            break
        elif status==True :
            print(f"Login gagal!\nAnda telah login dengan username {x}, silahkan lakukan “LOGOUT” sebelum melakukan login kembali.")
            break
        
 #   return (user,password)
#login(x,y)
x=input("Username : ")
y=input("Password : ")
login_system(x, y, user, password, status, loginu)