import unittest;
from Lab_one import lab_one
from Lab_two import lab_two
from Lab_three import lab_three
from Lab_four import calcArea
from Lab_five import lab_five
# from Lab_six import lab_six
class TestAssignmentOne(unittest.TestCase):
    def lab_one(self):
        self.assertEqual(lab_one('mobile'), 'mbl')
        self.assertEqual(lab_one('MOBILE'), 'MBL')
        self.assertEqual(lab_one('MobIlE'), 'Mbl')

    def lab_two(self):
        self.assertEqual(lab_two('This is javaScript','i'), [2,5,15])

    def lab_three(self):
        self.assertEqual(lab_three(3), [[1],[2,4],[3,6,9]])

    def calcArea(self):
        self.assertEqual(lab_two("r"),25.0)

    def lab_five(self):
        l1 = ["ahmed", "fatma", "ibrahim"]
        d1 = {'a':['ahmed'], 'f':['fatma'],'i':['ibrahim']}
        self.assertEqual(lab_five(l1), d1)

    







if __name__ == '__main__':
    unittest.main()