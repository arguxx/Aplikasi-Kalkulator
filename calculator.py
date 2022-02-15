class calc:
    def __init__(self,a=1,b=1,c=1,d=1):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
    def sum(self):
        print('Hasil dari perhitungan tersebut adalah {}'.format(self.a,self.b, self.a + self.b))

    def decrease(self):
        print('Hasil dari perhitungan tersebut adalah {}'.format(self.a,self.b, self.a - self.b))

    def division(self):
        print('Hasil dari perhitungan tersebut adalah {}'.format(self.a / self.b / self.c / self.d))

    def multiplication(self):
        print('Hasil dari perhitungan tersebut adalah {}'.format(self.a * self.b * self.c * self.d))


