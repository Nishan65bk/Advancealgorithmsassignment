import math

def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def geometric_median(points, eps=1e-6, max_iter=1000):
    x = sum(p[0] for p in points) / len(points)
    y = sum(p[1] for p in points) / len(points)

    for _ in range(max_iter):
        num_x = 0.0
        num_y = 0.0
        den = 0.0

        for px, py in points:
            d = math.hypot(x - px, y - py)
            if d == 0:
                continue
            w = 1 / d
            num_x += px * w
            num_y += py * w
            den += w

        if den == 0:
            break

        new_x = num_x / den
        new_y = num_y / den

        if distance((x, y), (new_x, new_y)) < eps:
            x, y = new_x, new_y
            break

        x, y = new_x, new_y

    return x, y

def total_distance(points, hub):
    return sum(distance(p, hub) for p in points)

def optimal_hub_distance(sensor_locations):
    hub = geometric_median(sensor_locations)
    result = total_distance(sensor_locations, hub)
    print("Time Complexity: O(N × K)")
    return round(result, 6)
