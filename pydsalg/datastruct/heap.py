def heapsort0(a):
    def heapify(a):
        count = len(a)
        ilastnode = len(a) - 1
        start = (ilastnode - 1) // 2

        while start >= 0:
            trickle_down(a, start, count)
            start -= 1

    def trickle_down(a, start, count):
        root = start

        while root * 2 + 1 < count:
            child = root * 2 + 1

            if child + 1 < count and a[child] < a[child+1]:
                child += 1

            if a[root] < a[child]:
                a[root], a[child] = a[child], a[root]
                root = child
            else:
                return

    heapify(a)
    end = len(a) - 1

    while end > 0:
        a[end], a[0] = a[0], a[end]
        trickle_down(a, 0, end)
        end -= 1
