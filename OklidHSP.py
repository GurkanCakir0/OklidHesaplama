import math

def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

points = [(1, 2), (4, 6), (7, 8), (2, 1)]
distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

min_distance = min(distances)

print(f"Her nokta çifti arasındaki mesafeler: {distances}")
print(f"Minimum mesafe: {min_distance}")
#DEneme yanılma yolu