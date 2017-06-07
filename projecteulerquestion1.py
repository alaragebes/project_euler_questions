class ProjectEulerQuestion1(object):
    """
    Question : If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    """

    def __init__ (self):
        self.all_elements = [number for number in range(0, 1000)] # [1, 2, 3, .... 999]
        self.remainder_elements = []
        self.total_sum = 0

    def calculate(self):
        for num in self.all_elements :
            if num % 3 == 0  or num % 5 == 0 :
                self.remainder_elements.append(num)
        self.addition()

    def addition (self):
        for stuff in self.remainder_elements :
            self.total_sum = self.total_sum + stuff
        print self.total_sum


result = ProjectEulerQuestion1()
result.calculate()
# 233168
