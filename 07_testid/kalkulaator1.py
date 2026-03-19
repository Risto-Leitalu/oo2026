import unittest

class Kalkulaator:
    sisu="0"
    def vajutus(self, nupp):
        self.sisu = nupp
        pass
    
    def ekraan(self):
        return self.sisu
    

class TestKalkulaator(unittest.TestCase):
    k=Kalkulaator()
    def test_algus(self):
        self.assertEqual(self.k.ekraan(), "0")
    def test_vajutus(self):
        self.k.vajutus("1")
        self.assertEqual(self.k.ekraan(), "1")

suite = unittest.TestLoader().loadTestsFromTestCase(TestKalkulaator)
runner = unittest.TextTestRunner(verbosity=1)
result = runner.run(suite)
print(f'Teste: {result.testsRun}')
