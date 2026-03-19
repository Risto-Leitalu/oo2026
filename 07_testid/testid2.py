import unittest

def pindala(a, b):
    kokku=0
    for nr in range(a):
        kokku +=b
    if kokku <0: kokku=-kokku
    return kokku
    #return a*b+1

class TestMath(unittest.TestCase):
    def test_pindala(self):
        self.assertEqual(pindala(3, 5), 15)
    
    def test_tyhi_pindala(self):
        self.assertEqual(pindala(0, 5), 0)
        
    def test_negatiivne_pindala(self):
        self.assertEqual(pindala(3, -5), 15)

suite = unittest.TestLoader().loadTestsFromTestCase(TestMath)
runner = unittest.TextTestRunner(verbosity=0)
result = runner.run(suite)
print(f'Tests run: {result.testsRun}')