#5a
#Part A: Interactive Emergency Network Simulator (MST Logic)
class EmergencyNetwork:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = []

    def add_road(self, u, v, weight):
        self.edges.append((weight, u, v))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def calculate_mst(self):
        # Sorting edges by weight (Greedy Strategy)
        self.edges.sort()
        parent = {node: node for node in self.nodes}
        rank = {node: 0 for node in self.nodes}
        mst = []
        
        for weight, u, v in self.edges:
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)
            if root_u != root_v:
                mst.append((u, v, weight))
                self.union(parent, rank, root_u, root_v)
        return mst

# Example Usage (Test Case Simulation)
network = EmergencyNetwork(["HQ", "Supply_A", "Supply_B", "Hub_1"])
network.add_road("HQ", "Supply_A", 10)
network.add_road("Supply_A", "Supply_B", 5)
network.add_road("HQ", "Hub_1", 15)
network.add_road("Supply_B", "Hub_1", 2)

mst_result = network.calculate_mst()
print(f"MST Roads: {mst_result}")
print("Time Complexity: O(E log E) or O(E log V)")