import math
def Solver(a,b,c):
    '''Function to solve quadratic equation'''
    if a==0:
        if b==0:
            if c==0:
                return 'VSN'
            else:
                return 'VN'
        else:
            x=-c/b
            x='{0:g}'.format(round(x,2))
            return f'{x}'
    else:
        delta=b**2-4*a*c
        if delta<0:
            return 'VN'
        elif delta==0:
            kq=-b/(2*a)
            kq='{0:g}'.format(round(kq,2))
            return f'{kq}'
        else:
            x1=(-b-math.sqrt(delta))/(2*a)
            x2=(-b+math.sqrt(delta))/(2*a)
            x1='{0:g}'.format(round(x1,2))
            x2='{0:g}'.format(round(x2,2))
            return f'{x1} {x2}'
# Python code to demonstrate working of unittest 
import unittest 
class TestStringMethods(unittest.TestCase):
   
    def setUp(self):
    # Method called to prepare the test fixture
        pass
    
    def tearDown(self):
    #Method called immediately after the test method has been called and the result recorded.
        pass
    def test_1(self): 
        self.assertEqual(Solver(0,0,0),"VSN")
    def test_2(self): 
        self.assertEqual(Solver(0,0,1), "VN")
    def test_3(self):
        self.assertEqual(Solver(1,2,1),("-1"))
    def test_4(self):
        self.assertEqual(Solver(3,0,0), ("1"))  
    def test_5(self):
        self.assertEqual(Solver(1,-8,-2), "-0.24 8.24")
    def test_6(self):
        self.assertEqual(Solver(1,0,1), "VN") 
    def test_7(self):
        self.assertEqual(Solver(1000000,-4251000,4312994), "1.67 2.58")  
    def test_8(self):
        self.assertEqual(Solver(0,2,1), "-0.5")  
    def test_9(self): 
        self.assertEqual(Solver(1,-5,6),"2 3")
    def test_10(self): 
        self.assertEqual(Solver(1,-8,-2), "-0.24 8.24")
    def test_11(self): 
        self.assertEqual(Solver(0,1,2), ("-2"))  
    def test_12(self): 
        self.assertEqual(Solver(0,-2,5), "2.5")
    def test_13(self): 
        self.assertEqual(Solver(5,0,5), "VN")
    def test_14(self): 
        self.assertEqual(Solver(2,4,15), "VN")
    def test_15(self): 
        self.assertEqual(Solver(0,0,0), "VSN")
if __name__ == '__main__': 
    unittest.main() 
suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)

