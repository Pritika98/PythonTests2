import unittest

class SampleTests1(unittest.TestCase):
    
    def test_method1(self):
        print('Failed test')
        self.assertEqual(True, False)

    def test_method2(self):
        print('Passed test')
        self.assertEqual(True, True)

    def test_method3(self):
        self.assertEqual(True, False)

    def test_method4(self):
        print('Random gibberish')
        self.assertEqual(True, True)

    def test_method5(self):
        throw ('some exception')

class SampleTests2(unittest.TestCase):
    
    def test_method1(self):
        print('Failed test')
        self.assertEqual(True, False)

    def test_method2(self):
        print('Passed test')
        self.assertEqual(True, True)

    def test_method3(self):
        self.assertEqual(True, False)

    def test_method4(self):
        print('Random gibberish')
        self.assertEqual(True, True)

    def test_method5(self):
        throw ('some exception')

   
if __name__ == '__main__':
    unittest.main()
