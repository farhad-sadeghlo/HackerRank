""" This app provides the path to find the princess.
The input data should be in the format of
--p
-b-
---
(b stands for bot, and p stands for princess)
and the result for this specific case would be
Go UP
Go RIGHT.

It works for any square size of grid 2*2, 3*3, 4*4, 5*5, ... """

class findingprincess:
    def __init__(self, size):
        self.size = int(size)
        self.grid = [input(f'please type in your row number {i+1}: ') for i in range(self.size)]
    def display_path_to_princess(self):

        row_count = 0
        col_count = 0
        for row in self.grid:
            row_count += 1
            for col in row:
                col_count += 1
                if col == 'b':
                    bot_loc = [row_count, col_count]
                elif col == 'p':
                    p_loc = [row_count, col_count]

            if col_count >= self.size:
                col_count = 0

        path_x = p_loc[0] - bot_loc[0]
        path_y = p_loc[1] - bot_loc[1]

        if path_x < 0:
            print('Go UP ' * abs(path_x))
        elif path_x > 0:
            print('Go DOWN ' * abs(path_x))

        if path_y > 0:
            print('Go RIGHT ' * abs(path_y))
        elif path_y < 0:
            print('Go LEFT ' * abs(path_y))

        return