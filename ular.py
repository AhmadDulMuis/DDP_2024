from animals import*

class ular(Animals):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super(). __init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun
    def cetak_ular(self):
        super().cetak()
        print("Design \t\t: ", self.design, "\nRacun \t\t: ", self.racun) 
anaconda = ular("Anaconda", "kambing", "Amazon", "bertelur", "belang", "Titak Berbisa")
anaconda.cetak_ular() 

sanca = ular("sanca", "ternak", "rawa", "bertelur", "Batik", "Titak Berbisa")
sanca.cetak_ular() 









