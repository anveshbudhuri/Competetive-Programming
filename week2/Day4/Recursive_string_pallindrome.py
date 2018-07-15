import unittest


def get_permutations(string):

    # Generate all permutations of the input string
    val = []
    n = len(string)
    if n == 0:
        return {''}
    list_string = list(string)
    permute(list_string, 0, n - 1,val)
    return set(val)
    
def permute(a, l, r, list1):
    if l == r:
        list1.append(toString(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r, list1)
            a[l], a[i] = a[i], a[l]


def toString(List):
    return ''.join(List)















# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
