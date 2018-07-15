import unittest


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def get_closing_paren(sentence, opening_paren_index):
    # Find the position of the matching closing parenthesis
    s1 = Stack()

    count =0
    for i in range(opening_paren_index,len(sentence)):
        if sentence[i]== "(":
            s1.push(sentence[i])
            # if i >= opening_paren_index:
            count += 1
        if sentence[i] == ")":
            temp = s1.pop()
            # if i >= opening_paren_index:
            count -= 1
            if count == 0:
                return i


    assert (), "ex"


# Tests

class Test(unittest.TestCase):
    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)

    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)

    def test_sentence(self):
        actual = get_closing_paren('Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.', 10)
        expected = 79
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
