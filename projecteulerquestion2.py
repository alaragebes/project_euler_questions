class ProjectEulerQuestion2 (object):

    def __init__(self):
        self.mylist = []
        self.even = []
        self.total_sum = 0
        self.even_number_sum = 0

    def fill_the_list (self):
        self.mylist = [1, 2]
        self.total_sum = sum(self.mylist)
        self.mylist.append(sum(self.mylist))
        while self.mylist[-1] <= 4000000 :
            self.total_sum = self.mylist[-2] + self.mylist[-1]
            self.mylist.append(self.total_sum)
            print self.mylist
        self.fill_the_even_list()

    def fill_the_even_list (self):
        for num in self.mylist :
            if num % 2 == 0 :
                self.even.append(num)
                self.even_number_sum = self.even_number_sum + self.even[-1]
        print self.even_number_sum

my = ProjectEulerQuestion2 ()
my.fill_the_list()
