
import random
from shapely.geometry import Polygon, Point

def generate_random_point_in_quadrilateral(xTL, yTL, xTR, yTR, xBR, yBR, xBL, yBL):
    # Define the quadrilateral using the provided corner coordinates
    coords = [(xTL, yTL), (xTR, yTR), (xBR, yBR), (xBL, yBL)]
    pgon = Polygon(coords)
    
    # Get the bounding box of the polygon
    min_x, min_y, max_x, max_y = pgon.bounds
    
    while True:
        random_point = Point(random.uniform(min_x, max_x), random.uniform(min_y, max_y))
        if pgon.contains(random_point):
            return random_point.x, random_point.y

print("Enter the coordinates of the four corners of the quadrilateral:")
xTL, yTL = map(float, input("Enter x and y for Top Left corner (separated by a space): ").split())
xTR, yTR = map(float, input("Enter x and y for Top Right corner (separated by a space): ").split())
xBR, yBR = map(float, input("Enter x and y for Bottom Right corner (separated by a space): ").split())
xBL, yBL = map(float, input("Enter x and y for Bottom Left corner (separated by a space): ").split())

xR, yR = generate_random_point_in_quadrilateral(xTL, yTL, xTR, yTR, xBR, yBR, xBL, yBL)
print(f"Random point inside the quadrilateral: ({xR}, {yR})")

