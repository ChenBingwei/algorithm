# Given the array orders, which represents the orders that customers have done in a restaurant. More
# specificallyorders[i]=[customerNamei,tableNumberi,foodItemi] where customerNamei is the name of the customer,
# tableNumberi is the table customer sit at, and foodItemi is the item customer orders.
# 
# Return the restaurant's “display table”. The “display table” is a table whose row entries denote how many of each
# food item each table ordered. The first column is the table number and the remaining columns correspond to each
# food item in alphabetical order. The first row should be a header whose first column is “Table”, followed by the
# names of the food items. Note that the customer names are not part of the table. Additionally, the rows should be
# sorted in numerically increasing order.
# 
# 
# 
# Example 1:
# 
# Input: orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5",
# "Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]] Output: [["Table","Beef Burrito","Ceviche",
# "Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]] Explanation: The
# displaying table looks like:
# Table,Beef Burrito,Ceviche,Fried Chicken,Water
# 3    ,0           ,2      ,1            ,0
# 5    ,0           ,1      ,0            ,1
# 10   ,1           ,0      ,0            ,0
#
# For the table 3: David
# orders "Ceviche" and "Fried Chicken", and Rous orders "Ceviche". For the table 5: Carla orders "Water" and
# "Ceviche". For the table 10: Corina orders "Beef Burrito". Example 2:
# 
# Input: orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],
# ["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]] Output: [["Table","Canadian Waffles",
# "Fried Chicken"],["1","2","0"],["12","0","3"]] Explanation: For the table 1: Adam and Brianna order "Canadian
# Waffles". For the table 12: James, Ratesh and Amadeus order "Fried Chicken". Example 3:
# 
# Input: orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]
# Output: [["Table","Bean Burrito","Beef Burrito","Soda"],["2","1","1","1"]]
# 
# 
# Constraints:
# 
# 1 <=orders.length <= 5 * 10^4
# orders[i].length == 3
# 1 <= customerNamei.length, foodItemi.length <= 20
# customerNamei and foodItemi consist of lowercase and uppercase English letters and the space character.
# tableNumberiis a valid integer between 1 and 500.
#
from typing import List


class Solution:
    @staticmethod
    def displayTable(orders: List[List[str]]) -> List[List[str]]:
        item_set = set()
        for i in orders:
            item_set.add(i[2])
        format_list = list(item_set)
        format_list.sort()
        order_dict = {v: n for n, v in enumerate(format_list)}
        talbe_dict = {}
        for i in orders:
            talbe_dict.setdefault(i[1], [0] * len(format_list))
            talbe_dict[i[1]][order_dict[i[2]]] += 1

        first_list = ["Table"] + format_list
        res_list = []
        for k, v in talbe_dict.items():
            tmp_list = [k] + list(map(str, v))
            res_list.append(tmp_list)
        res_list.sort(key=lambda x:int(x[0]))
        res_list.insert(0,first_list)
        return res_list

if __name__ == '__main__':
    res = Solution.displayTable(
        [
            ["David","3","Ceviche"],
            ["Corina","10","Beef Burrito"],
            ["David","3","Fried Chicken"],
            ["Carla","5","Water"],
            ["Carla","5","Ceviche"],
            ["Rous","3","Ceviche"]]
    )
    for i in res:
        print(i)