class Solution:

    def fix_fuel_config(self, config):
        config_vals = config.split(';')
        x_vals = [i.split(':')[0] for i in config_vals]
        if len(set(x_vals)) != len(x_vals):
            return "KEEP_PREVIOUS"
        config_tuples = [tuple([float(j) for j in i.split(':')]) for i in config_vals]
        mc_vals = []
        pt_nums = []
        for num,p1 in enumerate(config_tuples):
            p2 = config_tuples[(1- num//3)*(num+1)]
            slope = (p2[1]-p1[1])/(p2[0]-p1[0])
            intercept = (p2[0]*p1[1]-p1[0]*p2[1])/(p2[0]-p1[0])
            mc_vals.append((slope, intercept))
            pt_nums.append((num, (1- num//3)*(num+1)))
        #Added step to check length of slope values in order to 
        #deal with issues with float precision
        mc_vals = [tuple([round(j,2) if len(str(j))>6 else j for j in i]) for i in mc_vals]
        most_common_eval = max(set(mc_vals), key=mc_vals.count)
        most_common_count = mc_vals.count(most_common_eval)
        if most_common_count == 4:
            return config
        elif most_common_count == 2:
            eqn_check = [(float(i[1])==most_common_eval[0]*float(i[0]) + most_common_eval[1]) for i in config_tuples]
            odd_one_index = eqn_check.index(False)
            odd_one = config_vals[odd_one_index]
            x, y = odd_one.split(':')
            new_y = float(x) * most_common_eval[0] + most_common_eval[1]
            str_y = str(new_y)
            if str_y.split('.')[-1] == '0':
                new_y = round(new_y)
                str_y = str(new_y)
            new_val = x + ':' + str_y
            return config.replace(odd_one, new_val)
        else:
            return "KEEP_PREVIOUS"


import unittest
class SolutionTests(unittest.TestCase):

    
    def test1(self):
        solution = Solution()
        self.assertEqual(solution.fix_fuel_config("1:2;2:4;3.5:7;4:8"), "1:2;2:4;3.5:7;4:8")
    
    def test2(self):
        solution = Solution()
        self.assertEqual(solution.fix_fuel_config("1:1;2:5;3:3;4:6"), "KEEP_PREVIOUS")
    
    def test3(self):
        solution = Solution()
        self.assertEqual(solution.fix_fuel_config("1:1;1:2;3:3;4:4"), "KEEP_PREVIOUS")
    
    def test4(self):
        solution = Solution()
        self.assertEqual(solution.fix_fuel_config("1:1;2:2;3.5:3.5;4:5"), "1:1;2:2;3.5:3.5;4:4")
    
    def test5(self):
        solution = Solution()
        self.assertEqual(solution.fix_fuel_config("0:0;1:0;2:0;3:0"), "0:0;1:0;2:0;3:0")
    
    def test6(self):
        solution = Solution()
        self.assertEqual(solution.fix_fuel_config("5:1;10:2;2.5:12.5;12.5:2.5"), "5:1;10:2;2.5:0.5;12.5:2.5")
    
    def test7(self):
        solution = Solution()
        self.assertEqual(solution.fix_fuel_config("3:11;1:10;12.5:20.5;78:86"), "3:11;2:10;12.5:20.5;78:86")
    
    def test8(self):
        solution = Solution()
        self.assertEqual(solution.fix_fuel_config("1:100;2:2;3.5:3.5;4:4"), "1:1;2:2;3.5:3.5;4:4")
    
    def test9(self):
        solution = Solution()
        self.assertEqual(solution.fix_fuel_config("1:1;0:2;3.5:3.5;4:4"), "1:1;0:0;3.5:3.5;4:4")
    
    def test10(self):
        solution = Solution()
        self.assertEqual(solution.fix_fuel_config("1:1;2:2;70:35;4:5"), "1:1;2:2;70:70;4:4")
    
    def test11(self):
        solution = Solution()
        self.assertEqual(solution.fix_fuel_config("1:6;0.2:2;3.5:3.5;4:21"), "1:6;0.2:2;3.5:18.5;4:21")
    
    def test12(self):
        solution = Solution()
        self.assertEqual(solution.fix_fuel_config("5:1;10:2;1:3.5;12.5:2.5"), "5:1;10:2;1:0.2;12.5:2.5")

if __name__ == '__main__':
    unittest.main()