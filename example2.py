def checkValidDate(d, m ,y):
    '''Function to check date is valid or not'''
    max_day = 31
    if(m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
        max_day = 31
    elif(m == 4 or m == 6 or m == 9 or m == 11):
        max_day = 30
    elif(y % 4 == 0 and y % 100 != 0 or y % 400 == 0):
        max_day = 29
    else:
        max_day = 28
    if(m < 1 or m > 12):
        return 'Invalid'
    elif(d < 1 or d > max_day):
        return 'Invalid'
    return 'Valid'

# print(checkValidDate(28, 12, 2023))

import unittest
class TestStringMethods(unittest.TestCase):
       
    # Setting up for the test
    def setUp(self):
        pass
    
    # Cleaning up after the test
    def tearDown(self):
        pass
    def test_1(self): 
        self.assertEqual(checkValidDate(19, 5, 1890), 'Valid')
    def test_2(self): 
        self.assertEqual(checkValidDate(29,2,2023), 'Invalid')
    def test_3(self):
        self.assertEqual(checkValidDate(30,4,1975), 'Valid')
    def test_4(self):
        self.assertEqual(checkValidDate(31,6,2016), 'Invalid')  
    def test_5(self):
        self.assertEqual(checkValidDate(31,1,2020), 'Valid')
    def test_6(self):
        self.assertEqual(checkValidDate(2,9,1945), 'Valid') 
    def test_7(self):
        self.assertEqual(checkValidDate(12, 13, 2022), 'Invalid') 
    def test_8(self):
        self.assertEqual(checkValidDate(30, 2, 2020), 'Valid')  
    def test_9(self): 
        self.assertEqual(checkValidDate(33,3,2000), 'Invalid')
    def test_10(self): 
        self.assertEqual(checkValidDate(31, 12, 2022), 'Valid')
    def test_11(self): 
        self.assertEqual(checkValidDate(1, 1, 2019), 'Valid')  
    def test_12(self): 
        self.assertEqual(checkValidDate(31, 3, 2023), 'Valid')
    def test_13(self): 
        self.assertEqual(checkValidDate(12, 9 , 1989), 'Valid')
    def test_14(self): 
        self.assertEqual(checkValidDate(12, 0, 2000), 'Invalid')
    def test_15(self): 
        self.assertEqual(checkValidDate(31, 8, 2000), 'Valid')
if __name__ == '__main__': 
    unittest.main() 
suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
    