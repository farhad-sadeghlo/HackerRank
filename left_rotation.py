class leftRotation:
    def __init__(self, first_multiple_input, a):

        self.first_multiple_input = first_multiple_input.rstrip().split()
        self.n = int(self.first_multiple_input[0])
        self.d = int(self.first_multiple_input[1])
        self.a = list(map(int, a.rstrip().split()))
        self.i = None

    def leftRotate(self):

        i = 0
        temp = []
        for i in range(self.d, len(self.a)):

            temp.append(self.a[i])

        for i in range(self.d):

            temp.append(self.a[i])

        return print(temp)
