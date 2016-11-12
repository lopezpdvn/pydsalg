class HashTable0:
    _ARR_DEFAULT_LENGTH = 137
    """Map strings to objects"""
    def __init__(self, arr_size=_ARR_DEFAULT_LENGTH):
        # Instantiate lists until insertion
        self._arr = [None for i in range(arr_size)]
        self.length = arr_size
        self.count = 0

    def _hash_str_00(self, key):
        hashv = 0
        for c in key:
            hashv = (hashv * 27 + ord(c)) % self.length
        return hashv

    def __getitem__(self, key):
        index = self._hash_str_00(key)
        try:
            return self._arr[index][0]
        except (IndexError, TypeError):
            raise KeyError

    def __setitem__(self, key, value):
        # Emulate SortedLinkedList.Add
        index = self._hash_str_00(key)
        try:
            self._arr[index].append(value)
            self._arr[index].sort()
        except AttributeError:
            self._arr[index] = [value]

        self.count += 1

    def __contains__(self, key):
        index = self._hash_str_00(key)
        return self._arr[index]
