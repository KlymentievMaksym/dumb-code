class Lst:
    def __init__(self):
        self.lst = ['|', '|', '|']
        # self.lst_even = []
        # self.lst_neven = []
        # self.lst_odd = []
        # self.lst_nodd = []
        self.lst_dct = {-2:[], -1:[], 1:[], 2:[]}

    def sort(self, lst):
        killer=1
        was_changed = True
        while was_changed:
            was_changed  = False
            for index in range(len(lst)-killer):
                if lst[index] > lst[index+1]:
                    lst[index], lst[index+1] = lst[index+1], lst[index]
                    was_changed = True
            killer += 1

    def add(self, num, lst_num):
        lst = self.lst_dct[lst_num]
        lst += [num]
        self.sort(lst)



lst = input("Enter your list of INTEGER Numbers here (only numbers): ").split()
sort_method = input("Enter your type of sort here (default is 'negative even odd even negative odd'|'-2 1 2 -1'): ").split()

lst_sorted = Lst()

for number in lst:
    number = int(number)
    if number % 2 == 0:
        if number == abs(number):
            lst_sorted.add(number, 2)
        else:
            lst_sorted.add(number, -2)
    else:
        if number == abs(number):
            lst_sorted.add(number, 1)
        else:
            lst_sorted.add(number, -1)

print(lst_sorted.lst_dct)