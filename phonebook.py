class phonebook:

    def __init__(self, counter):

        self.counter = int(counter)
        self.phonebook = {}
        self.listofnames = []
        self.output = []

        for _ in range(self.counter):
            name, number = input('Please type in your phonebook entries: ').split()
            self.phonebook[name] = number

    def num_retriever(self):

        for _ in range(self.counter):
            self.listofnames.append(input('Please type the name you look for from phonebook: '))

        for name in self.listofnames:

            if name in self.phonebook.keys():

                self.output.append(f'{name}={self.phonebook[name]}')

            else:

                self.output.append('Not found')

        return print(*self.output, sep="\n")

