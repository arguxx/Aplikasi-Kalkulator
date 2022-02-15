from session import session
while True:
    print("1. Pembagian \n2. Penambahan \n3. Pengurangan \n4. Pengalian")
    insert = int(input("\ntolong pilih angka: "))   
    if insert == 1:
        session.ses_division()
    elif insert == 2:
        session.ses_sum()
    elif insert == 3:
        session.ses_decrease()
    elif insert == 4:
        session.ses_multiplication()
    elif insert == 5:
        print("Terima Kasih! >_<")
        break
    else:
        print("Masukan 1-4 >_<")


