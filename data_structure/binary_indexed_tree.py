class Bit:
    def __init__(self, n):
        self.size = n
        self.min_tree = [10 ** 18] * (n + 1)
        self.max_tree = [0] * (n + 1)
        self.sum_tree = [0] * (n + 1)

    def get_min(self, i):
        s = 10 ** 18
        while i > 0:
            s = min(s, self.min_tree[i])
            i -= i & -i
        return s

    def upd_min(self, i, x):
        while i <= self.size:
            self.min_tree[i] = min(x, self.min_tree[i])
            i += i & -i

    def get_max(self, i):
        s = -(10 ** 18)
        while i > 0:
            s = max(s, self.max_tree[i])
            i -= i & -i
        return s

    def upd_max(self, i, x):
        while i <= self.size:
            self.max_tree[i] = max(x, self.max_tree[i])
            i += i & -i

    def get_sum(self, i):
        s = 0
        while i > 0:
            s += self.sum_tree[i]
            i -= i & -i
        return s

    def upd_sum(self, i, x):
        while i <= self.size:
            self.sum_tree[i] += x
            i += i & -i

bit = Bit(9)
bit.upd_sum(1,2)
bit.upd_sum(3,5)
bit.upd_sum(5,3)
bit.upd_sum(2,1)
bit.upd_sum(6,7)
bit.upd_sum(8,2)
bit.upd_sum(9,1)
bit.upd_sum(4,6)
bit.upd_sum(7,8)
print(bit.sum_tree)
print(bit.get_sum(6))
