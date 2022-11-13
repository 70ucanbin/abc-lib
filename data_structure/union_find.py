class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = [-1] * n
        self.rank = [0] * n

    def find_root(self, x: int) -> int:
        if self.parent[x] == -1:
            return x
        return self.find_root(self.parent[x])

    def is_same(self, x: int, y: int) -> bool:
        return self.find_root(x) == self.find_root(y)

    def union_vertices(self, x: int, y: int) -> bool:
        x_root = self.find_root(x)
        y_root = self.find_root(y)
        if x_root == y_root:
            return 1
        else:
            if self.rank[x_root] > self.rank[y_root]:
                self.parent[y_root] = x_root
            elif self.rank[y_root] > self.rank[x_root]:
                self.parent[x_root] = y_root
            else:
                self.parent[x_root] = y_root
                self.rank[y_root] += 1
            return 0

edges = [[0,1],[1,2],[1,3],[3,4],[2,5],[5,4]]

uf = UnionFind(6)
for edge in edges:
    x, y = edge
    print(f"x: {x}, y: {y} Cycle: {uf.union_vertices(x,y)}")
