from random import randint

class DynamicArray:
    def __init__(self, initial_len=8, start=4):
        self.grow_factor = 2
        self.count = 0
        self.length = initial_len
        self._arr = [None,] * self.length
        #self._start = self._end = randint(0, self.length-1)
        self._start = self._end = start

    def append(self, value):
        if self.count == self.length:
            self._grow()

        self[self._end] = value
        if self._end == self.length - 1:
            self._end = 0
        else:
            self._end += 1
        self.count += 1

    def remove(self):
        if self.count == 0:
            raise DynamicArrayException()

        rt = self[self._start]
        if self._start == self.length - 1:
            self._start = 0
        else:
            self._start += 1
        self.count -= 1
        return rt

    def __getitem__(self, index):
        return self._arr[index]

    def __setitem__(self, index, value):
        self._arr[index] = value

    def _grow(self):
        newlength = self.length * self.grow_factor
        newarr = [None,] * newlength

        if self._end <= self._start:
            for i in range(self._end+1):
                newarr[i] = self._arr[i]
            for i in range(self._start, self.length):
                j = i + newlength - self.length
                newarr[j] = self._arr[i]
            newstart = self._start + (newlength - self.length)
            self._start = newstart
        else:
            for i in range(self._start, self._end+1):
                newarr[i] = self._arr[i]
            newend = self._end + (newlength - self.length)
            self._end = newend

        self.length = newlength
        self._arr = newarr

class DynamicArrayException(Exception):
    pass
