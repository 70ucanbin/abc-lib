
class SegTreeSum:
    """区間和を取得するためのセグメントツリー

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    sgt = SegTreeSum(len(a))
    sgt.build(a)
                                              index(value)

    |                                             1(78)                                               |
    |                                                            2(68)                                |
    |             3(10)             |             4(26)            |              5(42)               |
    |      6(3)     |      7(7)     |      8(11)    |      9(15)   |      10(19)    |      11(23)     |
    | 12(1) | 13(2) | 14(3) | 15(4) | 16(5) | 17(6) | 18(7) | 19(8)| 20(9) | 21(10) | 22(11) | 23(12) |
    """

    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n * 2)

    def build(self, arr):
        for i in range(self.size):
            self.tree[i+self.size] = arr[i]
        for i in range(self.size-1, 0, -1):
            self.tree[i] = self.tree[i*2] + self.tree[i*2+1]

    def upd(self, i, value):
        i += self.size - 1
        self.tree[i] = value
        while i > 1:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
            i >>= 1

    def query(self, left, right):
        res = 0
        left += self.size - 1
        right += self.size - 1
        while left <= right:
            if left == right:
                res += self.tree[left]
                break
            if left & 1:
                res += self.tree[left]
                left += 1
            if right+1 & 1:
                res += self.tree[right]
                right -= 1
            left >>= 1
            right >>= 1
        return res


class SegTreeMin:
    """区間内の最小値を取得するためのセグメントツリー

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    sgt = SegTreeMin(len(a))
    sgt.build(a)
                                               index(value)

    |                                              1(1)                                               |
    |                                                           2(5)                                  |
    |             3(1)              |              4(5)            |              5(9)                |
    |      6(1)     |      7(3)     |      8(5)     |     9(7)     |      10(9)    |      11(11)      |
    | 12(1) | 13(2) | 14(3) | 15(4) | 16(5) | 17(6) | 18(7) | 19(8)| 20(9) | 21(10) | 22(11) | 23(12) |
    """

    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n * 2)

    def build(self, arr):
        for i in range(self.size):
            self.tree[i+self.size] = arr[i]
        for i in range(self.size-1, 0, -1):
            self.tree[i] = min(self.tree[i*2], self.tree[i*2+1])

    def upd(self, i, value):
        i += self.size - 1
        self.tree[i] = value
        while i > 1:
            self.tree[i >> 1] = min(self.tree[i], self.tree[i ^ 1])
            i >>= 1

    def query(self, left, right):
        res = float('inf')
        left += self.size - 1
        right += self.size - 1
        while left <= right:
            if left == right:
                res = min(res, self.tree[left])
                break
            if left & 1:
                res = min(res, self.tree[left])
                left += 1
            if right+1 & 1:
                res = min(res, self.tree[right])
                right -= 1
            left >>= 1
            right >>= 1
        return res


class SegTreeMax:
    """区間内の最大値を取得するためのセグメントツリー

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    sgt = SegTreeMax(len(a))
    sgt.build(a)
                                               index(value)

    |                                             1(12)                                               |
    |                                                           2(12)                                 |
    |             3(4)              |              4(8)            |              5(12)               |
    |      6(2)     |      7(4)     |      8(6)     |     9(8)     |      10(10)    |      11(12)     |
    | 12(1) | 13(2) | 14(3) | 15(4) | 16(5) | 17(6) | 18(7) | 19(8)| 20(9) | 21(10) | 22(11) | 23(12) |
    """

    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n * 2)

    def build(self, arr):
        for i in range(self.size):
            self.tree[i+self.size] = arr[i]
        for i in range(self.size-1, 0, -1):
            self.tree[i] = max(self.tree[i*2], self.tree[i*2+1])

    def upd(self, i, value):
        i += self.size - 1
        self.tree[i] = value
        while i > 1:
            self.tree[i >> 1] = max(self.tree[i], self.tree[i ^ 1])
            i >>= 1

    def query(self, left, right):
        res = -1
        left += self.size - 1
        right += self.size - 1
        while left <= right:
            if left == right:
                res = max(res, self.tree[left])
                break
            if left & 1:
                res = max(res, self.tree[left])
                left += 1
            if right+1 & 1:
                res = max(res, self.tree[right])
                right -= 1
            left >>= 1
            right >>= 1
        return res
