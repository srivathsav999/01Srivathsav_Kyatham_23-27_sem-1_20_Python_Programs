import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def euclidean_distance(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance

# Example usage:
# Create two Point objects
point1 = Point(1, 2)
point2 = Point(4, 6)

# Calculate Euclidean distance
distance = point1.euclidean_distance(point2)

# Print the result
print(f"The Euclidean distance between the two points is: {distance}")
