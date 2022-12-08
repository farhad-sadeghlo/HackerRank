""" This app provides the path to find the princess.
The input data can be in any matrix format n*m. Just provide the number of rows n,
and be consistent with providing equal number of characters m (your columns) in each row.

---p
----
-b--
----

(b stands for bot, and p stands for princess)
and the result for this specific case would be

Go UP Go UP
Go RIGHT Go RIGHT

Other examples:

7*4
-b---
-----
-----
-----
-----
-----
---p-

or *23
---------------------p-
-----------------------
-----------------------
--b--------------------

or whatever you like"""

class findingprincess:
    def __init__(self, size):
        self.size = int(size)
        self.grid = [input(f'please provide contents of your row number {i+1}: ') for i in range(self.size)]
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