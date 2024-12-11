from animals import*

class ikan(Animals):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, ciri):
        super(). __init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.ciri = ciri
    def cetak_ikan(self):
        super().cetak()
        print("Design\t \t: ", self.design, "\nciri \t\t: ", self.ciri)
teri = ikan("teri", "plankton", "Laut", "bertelur", "abu-abu", "berkelompok")
teri.cetak_ikan()

lele = ikan("lele", "segala", "Empang", "bertelur", "hitam", "berkumis")
lele.cetak_ikan()