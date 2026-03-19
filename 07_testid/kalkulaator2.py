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
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestKalkulaator)
runner = unittest.TextTestRunner(verbosity=1)
result = runner.run(suite)
print(f'Teste: {result.testsRun}')

