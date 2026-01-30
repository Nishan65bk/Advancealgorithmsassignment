#qn4

def solve_energy_distribution():
    # Model Input Data
    demands = [
        {"hour": 6, "A": 20, "B": 15, "C": 25},
        {"hour": 7, "A": 22, "B": 16, "C": 28}
    ]

    sources = [
        {"id": "S1", "type": "Solar", "cap": 50, "start": 6, "end": 18, "cost": 1.0},
        {"id": "S2", "type": "Hydro", "cap": 40, "start": 0, "end": 24, "cost": 1.5},
        {"id": "S3", "type": "Diesel", "cap": 60, "start": 17, "end": 23, "cost": 3.0}
    ]

    districts = ["A", "B", "C"]
    total_cost = 0.0
    renewable_energy = 0.0
    total_energy_provided = 0.0

    print(f"{'Hour':<6} {'Dist':<6} {'Solar':<8} {'Hydro':<8} {'Diesel':<8} {'Used':<8} {'Dem':<8} {'% Met'}")
    print("-" * 70)

    for row in demands:
        hr = row["hour"]
        # Get and sort available sources by cost (Greedy)
        avail_sources = [s for s in sources if s["start"] <= hr <= s["end"]]
        avail_sources.sort(key=lambda x: x["cost"])
        
        # Track remaining capacity for this hour
        caps = {s["id"]: s["cap"] for s in avail_sources}

        for dist in districts:
            demand = row[dist]
            provided = {"S1": 0.0, "S2": 0.0, "S3": 0.0}
            current_total = 0.0

            for s in avail_sources:
                needed = demand - current_total
                if needed <= 0: break
                
                take = min(needed, caps[s["id"]])
                provided[s["id"]] = take
                caps[s["id"]] -= take
                current_total += take
                
                cost_inc = take * s["cost"]
                total_cost += cost_inc
                if s["type"] in ["Solar", "Hydro"]:
                    renewable_energy += take

            total_energy_provided += current_total
            met_pct = (current_total / demand) * 100
            
            # Output Row
            print(f"{hr:<6} {dist:<6} {provided['S1']:<8.1f} {provided['S2']:<8.1f} "
                  f"{provided['S3']:<8.1f} {current_total:<8.1f} {demand:<8.1f} {met_pct:.1f}%")

    # Analysis Report
    print("\n--- Analysis Report ---")
    print(f"Total Cost: Rs. {total_cost:.2f}")
    renewable_pct = (renewable_energy / total_energy_provided) * 100 if total_energy_provided > 0 else 0
    print(f"Renewable Energy Usage: {renewable_pct:.1f}%")
    print("Algorithm Complexity: O(H * D * S)")

if __name__ == "__main__":
    solve_energy_distribution()