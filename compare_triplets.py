class compareTriplets:
    def __init__(self, a, b):
        self.a = list(map(int, a.rstrip().split()))
        self.b = list(map(int, b.rstrip().split()))

    def compareTriplets(self):
        # Write your code here
        alice = 0
        bob = 0
        for i in range(3):
            if self.a[i] > self.b[i]:
                alice += 1
            elif self.a[i] < self.b[i]:
                bob += 1
            else:
                continue
        return print(alice, bob)

