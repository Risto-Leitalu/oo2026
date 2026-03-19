import unittest

class Kalkulaator:
    sisu="0"
    def vajutus(self, nupp):
        if self.sisu == "0":
            self.sisu=nupp
        else:
            self.sisu = self.sisu + nupp
        
    def ekraan(self):
        return self.sisu
    
    def puhasta(self):
        self.sisu = "0"
        return self.sisu

class TestKalkulaator(unittest.TestCase):
    k=Kalkulaator()
    def test_algus(self):
        self.assertEqual(self.k.ekraan(), "0")
        
    def test_vajutus_1(self):
        self.k.vajutus("1")
        self.assertEqual(self.k.ekraan(), "1")
        
    def test_vajutus_2(self):
        self.k.puhasta()
        self.k.vajutus("1")
        self.k.vajutus("2")
        self.assertEqual(self.k.ekraan(), "12")
    
    def test_liida(self):
        self.k.puhasta()
        self.k.vajutus("5")
        self.k.liida()
        self.k.vajutus("2")
        self.k.summa()
        self.assertEqual(self.k.ekraan(), "7")
    
    def test_korruta(self):
        self.k.puhasta()
        self.k.vajutus("9")
        self.k.korruta()
        self.k.vajutus("4")
        self.k.summa()
        self.assertEqual(self.k.ekraan(), "36")
    
    def test_jaga(self):
        self.k.puhasta()
        self.k.vajutus("9")
        self.k.jaga()
        self.k.vajutus("3")
        self.k.summa()
        self.assertEqual(self.k.ekraan(), "3")
    
suite = unittest.TestLoader().loadTestsFromTestCase(TestKalkulaator)
runner = unittest.TextTestRunner(verbosity=1)
result = runner.run(suite)
print(f'Teste: {result.testsRun}')
