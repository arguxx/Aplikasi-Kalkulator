from calculator import calcu
import session

print("1. two numbers \n2. three numbers \n3. Four Numbers \n4. exit")
insert = input()
while insert > 5 & insert != 0:
    print("1. two numbers \n2. three numbers \n3. Four Numbers \n4. exit")
    insert = input("\ntolong pilih angka: ")
    if insert == 1:
        print("berhasil memilih satu")
    elif insert == 2:
        print("berhasil memilih dua")

