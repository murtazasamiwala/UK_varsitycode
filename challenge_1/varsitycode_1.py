class ShoppingBag:

    def calculate_bag_total(self, items, discounts):
        # Your code goes here
        discount_dict = {}
        final_amt = []
        order_dict = {}
        for item in items:
            if item[:3] not in order_dict.keys():
                order_dict[item[:3]] = [int(item[3:]),1]
            else:
                order_dict[item[:3]][1] += 1
        for discount in discounts:
            if discount[:3] not in discount_dict.keys():
                discount_dict[discount[:3]] = []
                discount_dict[discount[:3]].append(discount[3:])
            else:
                discount_dict[discount[:3]].append(discount[3:])
        for item in order_dict.keys():
            if item not in discount_dict.keys():
                final_amt.append(order_dict[item][0]*order_dict[item][1])
            else:
                available_discounts = discount_dict[item]
                item_total, item_nos = order_dict[item][0] * order_dict[item][1], order_dict[item][1]
                best_price = item_total
                for disc in available_discounts:
                    if item_nos >= int(disc[0]):
                        if disc[1] == 'C':
                            curr_tot = item_total - int(disc[2:])*item_nos
                            if curr_tot < 0:
                                curr_tot = 0
                        else:
                            curr_tot = item_total * (1- (int(disc[2:])/100))
                        if (curr_tot < best_price) and (curr_tot >= 0):
                            best_price = curr_tot
                final_amt.append(best_price)
        return sum(final_amt)                              


import unittest

class ShoppingBagTests(unittest.TestCase):

    
    def test1(self):
        solution = ShoppingBag()
        self.assertEqual(solution.calculate_bag_total([ "ABC123" ], [ "ABC1P10" ]), 110.7)
    
    def test2(self):
        solution = ShoppingBag()
        self.assertEqual(solution.calculate_bag_total([ "ABC123" ], [ "ABC1C10" ]), 113)
    
    def test3(self):
        solution = ShoppingBag()
        self.assertEqual(solution.calculate_bag_total([ "ABC010","DEF020","ABC010" ], [ "ABC2P50","DEF1C05" ]), 25)
    
    def test4(self):
        solution = ShoppingBag()
        self.assertEqual(solution.calculate_bag_total([ "ABC123","ABC123" ], [ "ABC1P10" ]), 221.4)
    
    def test5(self):
        solution = ShoppingBag()
        self.assertEqual(solution.calculate_bag_total([ "ABC008" ], [ "ABC1P05" ]), 7.6)
    
    def test6(self):
        solution = ShoppingBag()
        self.assertEqual(solution.calculate_bag_total([ "ABC123","ABC123" ], [ "ABC1C10" ]), 226)
    
    def test7(self):
        solution = ShoppingBag()
        self.assertEqual(solution.calculate_bag_total([ "ABC008" ], [ "ABC1C05" ]), 3)
    
    def test8(self):
        solution = ShoppingBag()
        self.assertEqual(solution.calculate_bag_total([ "ABC123" ], [ "DEF1P10" ]), 123)
    
    def test9(self):
        solution = ShoppingBag()
        self.assertEqual(solution.calculate_bag_total([ "ABC123" ], [ "" ]), 123)
    
    def test10(self):
        solution = ShoppingBag()
        self.assertEqual(solution.calculate_bag_total([  ], [ "ABC1P10" ]), 0)
    
    def test11(self):
        solution = ShoppingBag()
        self.assertEqual(solution.calculate_bag_total([  ], [  ]), 0)
    
    def test12(self):
        solution = ShoppingBag()
        self.assertEqual(solution.calculate_bag_total([ "ABC123","ABC123" ], [ "ABC2P10" ]), 221.4)
    
    def test13(self):
        solution = ShoppingBag()
        self.assertEqual(solution.calculate_bag_total([ "ABC123","ABC123" ], [ "ABC3P10" ]), 246)
    
    def test14(self):
        solution = ShoppingBag()
        self.assertEqual(solution.calculate_bag_total([ "ABC123","ABC123" ], [ "ABC2C10" ]), 226)
    
    def test15(self):
        solution = ShoppingBag()
        self.assertEqual(solution.calculate_bag_total([ "ABC123","ABC123" ], [ "ABC3C10" ]), 246)
    
    def test16(self):
        solution = ShoppingBag()
        self.assertEqual(solution.calculate_bag_total([ "ABC123","BCD012" ], [ "ABC1P10","BCD1C10" ]), 112.7)
    
    def test17(self):
        solution = ShoppingBag()
        self.assertEqual(solution.calculate_bag_total([ "ABC005","BCD020" ], [ "ABC1C10" ]), 20)
    
    def test18(self):
        solution = ShoppingBag()
        self.assertEqual(solution.calculate_bag_total([ "ABC200" ], [ "ABC1C10","ABC1C20" ]), 180)
    
    def test19(self):
        solution = ShoppingBag()
        self.assertEqual(solution.calculate_bag_total([ "ABC200" ], [ "ABC1P10","ABC1P20" ]), 160)
    
    def test20(self):
        solution = ShoppingBag()
        self.assertEqual(solution.calculate_bag_total([ "ABC200" ], [ "ABC1C10","ABC1P10" ]), 180)
    
    def test21(self):
        solution = ShoppingBag()
        self.assertEqual(solution.calculate_bag_total([ "ABC050" ], [ "ABC1C10","ABC1P10" ]), 40)
    
    def test22(self):
        solution = ShoppingBag()
        self.assertEqual(solution.calculate_bag_total([ "ABC050","BCD020","BCD020","ABC050","BCD020","CDE020","EFG200","EFG200" ], [ "ABC3C40","ABC3P50","ABC2P10","BCD2C30","ABC2C05","ABC1P20","ABC1C05","DEF1C10","EFG3C40","EFG3P50","EFG2P10","EFG2C05","EFG1P20","EFG1C50" ]), 400)

if __name__ == '__main__':
    unittest.main()                                    