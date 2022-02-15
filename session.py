from calculator import sum_min, mul_div
class session:
    def ses_division():
        input1 = int(input("masukan angka: "))
        input2 = int(input("masukan angka: "))        
        add_more = int(input("Tambah lagi? \n1. yes\n2. no: "))
        if add_more == 1:
            input3 = int(input("masukan angka: "))
            add_more = int(input("Tambah lagi? \n1. yes\n2. no\n"))
            if add_more == 1:
                input4 = int(input("masukan angka: "))
                hasil = mul_div(input1,input2,input3,input4)
                hasil.division()
            elif add_more == 2:
                hasil = mul_div(input1,input2,input3)
                hasil.division()    
        elif add_more == 2:
            hasil = mul_div(input1, input2)
            hasil.division()
    def ses_sum():
        input1 = int(input("masukan angka: "))
        input2 = int(input("masukan angka: "))        
        add_more = int(input("Tambah lagi? \n1. yes\n2. no: "))
        if add_more == 1:
            input3 = int(input("masukan angka: "))
            add_more = int(input("Tambah lagi? \n1. yes\n2. no\n"))
            if add_more == 1:
                input4 = int(input("masukan angka: "))
                hasil = sum_min(input1,input2,input3,input4)
                hasil.sum()
            elif add_more == 2:
                hasil = sum_min(input1,input2,input3)
                hasil.sum()   
        elif add_more == 2:
            hasil = sum_min(input1, input2)
            hasil.sum()
    def decrease():
        input1 = int(input("masukan angka: "))
        input2 = int(input("masukan angka: "))        
        add_more = int(input("Tambah lagi? \n1. yes\n2. no: "))
        if add_more == 1:
            input3 = int(input("masukan angka: "))
            add_more = int(input("Tambah lagi? \n1. yes\n2. no\n"))
            if add_more == 1:
                input4 = int(input("masukan angka: "))
                hasil = sum_min(input1,input2,input3,input4)
                hasil.decrease()
            elif add_more == 2:
                hasil = sum_min(input1,input2,input3)
                hasil.decrease()    
        elif add_more == 2:
            hasil = sum_min(input1, input2)
            hasil.decrease()
    def multiplication():
        input1 = int(input("masukan angka: "))
        input2 = int(input("masukan angka: "))        
        add_more = int(input("Tambah lagi? \n1. yes\n2. no: "))
        if add_more == 1:
            input3 = int(input("masukan angka: "))
            add_more = int(input("Tambah lagi? \n1. yes\n2. no\n"))
            if add_more == 1:
                input4 = int(input("masukan angka: "))
                hasil = mul_div(input1,input2,input3,input4)
                hasil.multiplication()
            elif add_more == 2:
                hasil = mul_div(input1,input2,input3)
                hasil.multiplication()    
        elif add_more == 2:
            hasil = mul_div(input1, input2)
            hasil.multiplication()