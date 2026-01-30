#1. Interactive Emergency Network Simulator (GUI)

import tkinter as tk
from tkinter import messagebox

# --- 1.a: Backend Logic (Kruskal's MST) ---
def get_mst_logic(nodes, edges):
    edges.sort(key=lambda x: x[2])
    parent = {node: node for node in nodes}
    def find(i):
        if parent[i] == i: return i
        parent[i] = find(parent[i])
        return parent[i]

    mst = []
    for u, v, w in edges:
        root_u, root_v = find(u), find(v)
        if root_u != root_v:
            parent[root_u] = root_v
            mst.append((u, v, w))
    return mst

# --- 1.b: GUI Implementation ---
class EmergencyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Emergency Network Simulator")
        
        # Data storage
        self.cities = {"HQ": (50, 50), "Hub_1": (250, 50), "Supply_A": (50, 200), "Supply_B": (250, 200)}
        self.roads = [("HQ", "Hub_1", 15), ("HQ", "Supply_A", 10), ("Supply_A", "Supply_B", 5), ("Supply_B", "Hub_1", 2)]
        
        # Canvas for visualization
        self.canvas = tk.Canvas(root, width=400, height=300, bg="white")
        self.canvas.pack()
        
        # Control Panel
        btn_mst = tk.Button(root, text="Visualize MST", command=self.draw_mst)
        btn_mst.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.draw_network()

    def draw_network(self):
        self.canvas.delete("all")
        # Draw Roads
        for u, v, w in self.roads:
            x1, y1 = self.cities[u]
            x2, y2 = self.cities[v]
            self.canvas.create_line(x1, y1, x2, y2, fill="gray", dash=(4,4))
            self.canvas.create_text((x1+x2)/2, (y1+y2)/2, text=str(w))
        
        # Draw Cities
        for name, (x, y) in self.cities.items():
            color = "red" if name == "HQ" else "blue"
            self.canvas.create_oval(x-10, y-10, x+10, y+10, fill=color)
            self.canvas.create_text(x, y-20, text=name)

    def draw_mst(self):
        mst_edges = get_mst_logic(list(self.cities.keys()), self.roads)
        self.draw_network() # Reset view
        for u, v, w in mst_edges:
            x1, y1 = self.cities[u]
            x2, y2 = self.cities[v]
            self.canvas.create_line(x1, y1, x2, y2, fill="green", width=3)
        messagebox.showinfo("Analysis", "MST Calculated using Kruskal's Algorithm\nComplexity: O(E log E)")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmergencyGUI(root)
    root.mainloop()