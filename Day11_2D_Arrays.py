# the following code provides the 3 by 3 part of a 6,6 matrix which its values are the
# highest in that 6 by 6 matrix

import numpy as np

class HourGlass:

    def __init__(self):
        values = ''.join(f'{input()} ' for _ in range(6))
        values = list(map(int, values.split()))
        self.glass = np.array(values).reshape(6, 6)
        self.hourglass_sum = 0
        self.hourglass = []

    def hourglass_function(self):
        for i in range(4):
            for j in range(4):
                if self.hourglass_sum < sum(sum(self.glass[i:i+3, j:j+3])):
                    self.hourglass_sum += sum(sum(self.glass[i:i+3, j:j+3]))
                    self.hourglass = self.glass[i:i+3, j:j+3]
        return print(self.hourglass)
