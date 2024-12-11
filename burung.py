from animals import*

class burung(Animals):
    def __init__(self, nama, makanan, hidup, berkembang_biak, terbang, cakar_tajam):
        super(). __init__(nama, makanan, hidup, berkembang_biak)
        self.terbang = terbang
        self.cakar_tajam = cakar_tajam
    def cetak_burung(self):
        super().cetak()
        print("aktifitas \t: ", self.terbang, "\nciri \t\t: ", self.cakar_tajam)

elang = burung("Elang", "burung", "Pohon", "bertelur", "Terbang", "cakar_tajam")
elang.cetak_burung()

puyuh = burung("puyuh", "burung", "semak", "bertelur", "berjalan&terbang", "kaki_kuat")
puyuh.cetak_burung()

