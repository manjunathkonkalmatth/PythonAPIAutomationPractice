import unittest

def setUpModule():
    print('Before Module')

def tearDownModule():
    print('After Module')

class TestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Before each class')

    @classmethod
    def tearDownClass(cls):
        print('After each class')

    def setUp(self):
        print('Before each test method')

    def tearDown(self):
        print('after each test method')

    def test_method1(self):
        print('test method1')

    def test_method2(self):
        print('test method2')


if __name__ == '__main__':
    unittest.main()
