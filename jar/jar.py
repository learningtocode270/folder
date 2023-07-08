class Jar:
    def __init__(self, capacity=100):
        jar = list(range(capacity))
        if capacity < 0:
            raise ValueError('needs to be a positive integer')
        self._capacity = capacity
        self._size = 6

    def __str__(self):
        return self.size * '🍪'

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("too many cookies in the jar. they won't fit")
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("There aren't that many")
        self._size -=  n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

jar = Jar()

# ADD cookies
a = int(input("add cookies: "))
jar.deposit(a)

# SUBTRACT cookies
s = int(input("take out cookies: "))
jar.withdraw(s)

# Print allowed number of cookies

# Show cookies in the jar
print(jar)
