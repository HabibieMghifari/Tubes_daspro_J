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
