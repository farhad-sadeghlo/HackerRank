class factorial:

    def __init__(self, num):

        self.num = int(num)

    def factorial_of_num(self):

        factorial_nums = {0: 1}

        for i in range(1, self.num + 1):

            factorial_nums[i] = int(i) * factorial_nums[i - 1]

        return print(factorial_nums[self.num])
