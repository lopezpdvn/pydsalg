class HashSetString:
    _ARR_DEFAULT_LENGTH = 211
    def __init__(self, arr_len=_ARR_DEFAULT_LENGTH):
        self._arr = [None,] * arr_len
        self._count = 0

    def _hash_str_00(self, value):
        hashv = 0
        for c in value:
            hashv = (hashv * 27 + ord(c)) % len(self._arr)
        return hashv
    hashf = _hash_str_00

    def __contains__(self, value):
        return self._arr[self.hashf(value)]

    def __iter__(self):
        return self._iterator()

    def __len__(self):
        return self._count

    def _iterator(self):
        return (val for val in self._arr if val)

    def add(self, value):
        index = self.hashf(value)
        if not self._arr[index]:
            self._arr[index] = value
            self._count += 1

    def remove(self, value):
        index = self.hashf(value)
        if self._arr[index]:
            self._arr[index] = None
            self._count -= 1
        else:
            raise KeyError
