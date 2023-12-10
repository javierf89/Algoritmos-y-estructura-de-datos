class BidirectionalFibonacciIterator:
    def __init__(self):
        self.current = 0
        self.next_value = 1
        self.prev_value = None
        self.backward = False

    def next(self):
        if self.prev_value is not None:
            self.current, self.next_value, self.prev_value = (
                self.next_value,
                self.current + self.next_value,
                None,
            )
            self.backward = False
            return self.current
        elif self.current == 0:
            self.prev_value = self.current
            self.backward = False
            return self.current
        else:
            self.current, self.next_value = self.next_value, self.current + self.next_value
            self.backward = False
            return self.current

    def previous(self):
        if self.backward:
            self.next()
            return self.current

        if self.prev_value is None:
            self.backward = True
            return self.current
        else:
            self.current, self.next_value, self.prev_value = (
                self.prev_value,
                self.current - self.prev_value,
                None if self.current == self.prev_value else self.current,
            )
            return self.current

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

# Example usage:
fibonacci_iter = BidirectionalFibonacciIterator()

# Forward iteration
for _ in range(10):
    print(next(fibonacci_iter), end=' ')
print()

# Backward iteration
for _ in range(10):
    print(fibonacci_iter.previous(), end=' ')
print()
