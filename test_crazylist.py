import unittest
import crazylist


class Tests(unittest.TestCase):
    lst = crazylist.Lst()

    def test_input(self):
        self.lst.ask_for_input("-12 13 -14 15 -16 17",
                               "-2 1 2 -1", True)
        self.assertEqual(self.lst.list,
                         ['-12', '13', '-14', '15', '-16', '17'])
        self.assertEqual(self.lst.sort_method, ['-2', '1', '2', '-1'])

    def test_sort(self):
        self.assertEqual(self.lst.sort([12, -1, 0.5, 123, -1234, 10/3]),
                         [-1234, -1, 0.5, 10/3, 12, 123])

    def test_add(self):
        self.lst.add(14, 2)
        self.lst.add(2, 2)
        self.lst.add(12, 2)
        self.assertEqual(self.lst.lst_dct[2], [2, 12, 14])
        self.lst.lst_dct[2] = []

    def test_start_app(self):
        self.lst.start_app()
        self.assertEqual(self.lst.lst,
                         [-16, -14, -12, '|', 13, 15, 17, '|', '|'])

    def test_bad_input(self):
        lst = crazylist.Lst()
        lst.ask_for_input("a b s", "a b s", True)
        lst.start_app(False)
        self.assertEqual(lst.lst, ['|', '|', '|'])
        lst = crazylist.Lst()
        lst.ask_for_input("a b s", "-2 1 2 -1", True)
        lst.start_app(False)
        self.assertEqual(lst.lst, ['|', '|', '|'])
        lst = crazylist.Lst()
        lst.ask_for_input("12 41 -12 -9 0 13 14", "a b s", True)
        lst.start_app(False)
        self.assertEqual(lst.lst, [-12, '|', 13, 41, '|', 0, 12, 14, '|', -9])
        lst = crazylist.Lst()
        lst.ask_for_input("12 41 -12 -9 0 13 14", "-2 1 2", True)
        lst.start_app(False)
        self.assertEqual(lst.lst, [-12, '|', 13, 41, '|', 0, 12, 14])
        lst = crazylist.Lst()
        lst.ask_for_input("12 41 -12 -9 0 13 14", "1 1 1 1", True)
        lst.start_app(False)
        self.assertEqual(lst.lst,
                         [13, 41, '|', 13, 41, '|', 13, 41, '|', 13, 41])


if __name__ == '__main__':
    unittest.main()
