# import random
import sys

class Lst:
    def __init__(self):
        self.lst = []
        
        self.lst_dct = {-2:[], -1:[], 1:[], 2:[]}
        self.dct = {"negeven":-2, "negodd":-1, "odd":1, "even":2}

    def ask_for_input(self):
        # random.sample(range(-100, 100), 25) 
        self.list = input("Enter your list of INTEGER Numbers here (empty to exit): ").split()
        if self.list == []:
            sys.exit()
        self.sort_method = input("Enter your type of sort here (default is 'negeven odd even negodd'|'-2 1 2 -1'): ").split()
        if self.sort_method == []:
            sys.exit()

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

    def rearrange_items(self):
        for number in self.list:
            try:
                number = int(number)
                if number % 2 == 0:
                    if number == abs(number):
                        self.add(number, 2)
                    else:
                        self.add(number, -2)
                else:
                    if number == abs(number):
                        self.add(number, 1)
                    else:
                        self.add(number, -1)
            except ValueError:
                print("Bad number element:", number, "| Skipping...")

    def change_all_type_to_num(self):
        for item in self.sort_method.copy():
            try:
                # print(int(item))
                num_typ = int(item)
                self.sort_method[self.sort_method.index(item)] = num_typ
            except ValueError:
                try:
                    # print(self.dct[item], item)
                    num_typ = self.dct[item]
                    self.sort_method[self.sort_method.index(item)] = num_typ
                except KeyError:
                    print("Bad key element:", item, "| Skipping...")
                    self.sort_method.pop(self.sort_method.index(item))

    def create_position(self, lst_num, need_split=True):
        if need_split:
            self.lst.extend(self.lst_dct[lst_num] + ['|'])
        else:
            self.lst.extend(self.lst_dct[lst_num])
    
    def start_app(self):
        lst.rearrange_items()
        lst.change_all_type_to_num()
        for pos in range(len(self.sort_method)):
            if pos == len(self.sort_method)-1:
                self.create_position(self.sort_method[pos], False)
            else:
                self.create_position(self.sort_method[pos])
        if self.lst == []:
            print("The list is empty because of bad type of sort entered | Using defaults...")
            for pos in [-2, 1, 2, -1]:
                if pos == -1:
                    self.create_position(pos, False)
                else:
                    self.create_position(pos)
        

    def display(self):
        self.lst_str = self.lst.copy()
        for item in self.lst_str:
            self.lst_str[self.lst_str.index(item)] = str(item)
        print("[" + " ".join(self.lst_str) + "]")


if __name__ == "__main__":
    while True:
        lst = Lst()
        lst.ask_for_input()
        lst.start_app()
        lst.display()
