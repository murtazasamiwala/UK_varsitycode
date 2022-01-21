class Solution:

    def number_of_days_to_save(self, moneySaved):
        total = 0
        day = 0
        last_monday = 0
        #day of week
        if 0 <= moneySaved < 74926:
            while total < moneySaved:
                day+=1
                dow = day - 7 * ((day-1)//7) -1
                if dow != 0:
                    total+=dow + last_monday
                else:
                    last_monday+=1
                    total+=last_monday+dow 
            return day
        
        else:
            return -1

import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        solution = Solution()
        self.assertEqual(solution.number_of_days_to_save(8), 4)
    
    def test2(self):
        solution = Solution()
        self.assertEqual(solution.number_of_days_to_save(36), 10)
    
    def test3(self):
        solution = Solution()
        self.assertEqual(solution.number_of_days_to_save(0), 0)
    
    def test4(self):
        solution = Solution()
        self.assertEqual(solution.number_of_days_to_save(55), 13)
    
    def test5(self):
        solution = Solution()
        self.assertEqual(solution.number_of_days_to_save(56), 14)
    
    def test6(self):
        solution = Solution()
        self.assertEqual(solution.number_of_days_to_save(74778), 999)
    
    def test7(self):
        solution = Solution()
        self.assertEqual(solution.number_of_days_to_save(74779), 1000)
    
    def test8(self):
        solution = Solution()
        self.assertEqual(solution.number_of_days_to_save(33900), 665)
    
    def test9(self):
        solution = Solution()
        self.assertEqual(solution.number_of_days_to_save(74927), -1)
    
    def test10(self):
        solution = Solution()
        self.assertEqual(solution.number_of_days_to_save(-1), -1)

if __name__ == '__main__':
    unittest.main()