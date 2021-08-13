class LimitedPrinter:
    def __init__(self, limit):
        self.starter = 10
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.starter > self.limit:
            raise StopIteration()

        self.starter += 1
        return self.starter


limited = LimitedPrinter(15)

for i in limited:
    print(i)

# for i in range(0, 10):
# next(limited)
