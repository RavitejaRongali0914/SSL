class SetMenu():
    def __init__(self,items):
        self.items= set(items)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        a=''
        for x in self.items :
            a += str(x) + "\n"
        return a
