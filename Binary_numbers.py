"""Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the
maximum number of consecutive 1's in n's binary representation. When working with different bases,
it is common to show the base as a subscript.

Example

The binary representation of (125)10 is (1111101)2. In base 2, there are 5 and 1 consecutive ones in two groups.
Print the maximum, 5."""
class Binary_num:

    def __init__(self, num):

        self.remainder = None
        self.binary = ''
        self.num = int(num)
        self.counter = 0
        self.bin_counter = []

    def Binary_maker(self):

        while self.num >= 2:

            self.binary += str(self.num % 2)
            divisor = self.num // 2

            if divisor >= 2:

                self.num = divisor

            else:

                self.binary += str(divisor)

            self.num = divisor

        binary = self.binary[::-1]

        for bin_num in binary:

            if bin_num == '1':

                self.counter += 1

            elif bin_num == '0':

                self.counter = 0

            self.bin_counter.append(self.counter)

        return print(max(self.bin_counter))
