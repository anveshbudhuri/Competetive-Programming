import unittest

def find_duplicate(list):
    """find a duplicate of 1..n in a list n+1 elements long"""

    n = len(list)
    ptr_1 = n
    ptr_2 = n
    # print("value 1 : " + str(list[ptr_1 - 1]) + "      value 2 : " + str(list[ptr_2 - 1]))
    while True:
        ptr_1 = list[ptr_1-1]
        ptr_2 = list[list[ptr_2-1]]
        # ptr_2 = list[ptr_2-1]
        # print("value 1 : " + str(list[ptr_1 - 1]) + "      value 2 : " + str(list[ptr_2 - 1]))
        if ptr_1 == ptr_2:
            # print(list[ptr_1-1])
            break

    ptr_2 = n
    while True:
        ptr_1 = list[ptr_1-1]
        ptr_2 = list[ptr_2-1]
        if ptr_2 == ptr_1:
            # print("value : "+str(ptr_1))
            return ptr_1





# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_duplicate([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_duplicate([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_duplicate([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_duplicate([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_duplicate([5, 1, 4, 8, 3, 2, 7, 6, 4])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
