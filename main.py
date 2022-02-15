from calculator import calc
while True:
    print("1. two numbers \n2. three numbers \n3. Four Numbers \n4. exit")
    insert = int(input("\ntolong pilih angka: "))
    if insert == 1:
        input1 = int(input("masukan angka: "))
        input2 = int(input("masukan angka: "))        
        add_more = int(input("Tambah lagi? \n1. yes\n2. no: "))
        if add_more == 1:
            input3 = int(input("masukan angka: "))
            add_more = int(input("Tambah lagi? \n1. yes\n2. no\n"))
            if add_more == 1:
                input4 = int(input("masukan angka: "))
                hasil = calc(input1,input2,input3,input4)
                hasil.division()
            elif add_more == 2:
                hasil = calc(input1,input2,input3)
                hasil.division()    
        elif add_more == 2:
            hasil = calc(input1, input2)
            hasil.division()
    elif insert == 2:
        print("berhasil memilih dua")
    elif insert == 3:
        print("berhasil memilih tiga")
    elif insert == 4:
        print("Thankyou :D")
        break
    else:
        print("Masukan 1-4 >_<")


