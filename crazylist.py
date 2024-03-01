import random

class Lst:
    def __init__(self):
        self.lst = []
        # self.lst_even = []
        # self.lst_neven = []
        # self.lst_odd = []
        # self.lst_nodd = []
        self.lst_dct = {-2:[], -1:[], 1:[], 2:[]}
        self.dct = {"negeven":-2, "negodd":-1, "odd":1, "even":2}

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

    def create_position(self, lst_num, need_split=True):
        if need_split:
            self.lst.extend(self.lst_dct[lst_num] + ['|'])
        else:
            self.lst.extend(self.lst_dct[lst_num])
    
    def start(self, lst_of_type):
        for item in lst_of_type:
            # print(lst_of_type)
            try:
                num_typ = int(item)
            except ValueError:
                num_typ = self.dct[item]
            lst_of_type[lst_of_type.index(item)] = num_typ
        for pos in range(len(lst_of_type)-1):
            self.create_position(lst_of_type[pos])
        self.create_position(lst_of_type[-1], False)

    def display(self):
        self.lst_str = self.lst.copy()
        for item in self.lst_str:
            self.lst_str[self.lst_str.index(item)] = str(item)
        print("[" + " ".join(self.lst_str) + "]")


lst = random.sample(range(-100, 100), 25)#input("Enter your list of INTEGER Numbers here (only numbers): ").split()
sort_method = input("Enter your type of sort here (default is 'negeven odd even negodd'|'-2 1 2 -1'): ").split()

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
    
lst_sorted.start(sort_method)
lst_sorted.display()
