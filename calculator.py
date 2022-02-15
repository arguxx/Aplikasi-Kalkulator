class mul_div:
    def __init__(self,a=1,b=1,c=1,d=1):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
    def division(self):
        print('Hasil dari perhitungan tersebut adalah {}'.format(self.a / self.b / self.c / self.d))

    def multiplication(self):
        print('Hasil dari perhitungan tersebut adalah {}'.format(self.a * self.b * self.c * self.d))

class sum_min:
        def __init__(self,a=0,b=0,c=0,d=0):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
        def sum(self):
            print('Hasil dari perhitungan tersebut adalah {}'.format(self.a + self.b + self.c + self.d))

        def decrease(self):
            print('Hasil dari perhitungan tersebut adalah {}'.format(self.a - self.b - self.c - self.d))
