# Random-Point-Inside-Quadrilateral


#Steps and Algorithms Used

1. Defining the Quadrilateral:
   - The quadrilateral is defined using the coordinates of its four corners.
   - The coordinates are used to create a `Polygon` object using the Shapely library.

2. Bounding Box Calculation:
   - The bounding box of the polygon is calculated. This is the smallest rectangle that completely contains the polygon.
   - The bounding box provides minimum and maximum values for both x and y coordinates (`min_x`, `min_y`, `max_x`, `max_y`).

3. Random Point Generation:
   - Random points are generated within the bounding box.
   - For each point, a random x-coordinate and a random y-coordinate are generated within the bounds (`min_x`, `max_x`) and (`min_y`, `max_y`), respectively.

4. Point-in-Polygon Check:
   - For each generated point, a check is performed to determine if the point lies inside the quadrilateral.
   - This check is done using the `contains` method from Shapely, which uses the **Ray-Casting Algorithm**.

#Ray-Casting Algorithm (Even-Odd Rule)

Steps of the Ray-Casting Algorithm:

1. Draw a Ray:
   - From the point in question, draw an imaginary horizontal ray to infinity in one direction (commonly to the right).

2. Count Intersections:
   - Count how many times the ray intersects with the edges of the polygon.

3. Determine Inside or Outside:
   - If the number of intersections is odd, the point is considered to be inside the polygon.
   - If the number of intersections is even, the point is considered to be outside the polygon.

Example:

Consider a quadrilateral with the following vertices:
- Top Left (TL): (2, 4)
- Top Right (TR): (4, 4)
- Bottom Right (BR): (4, 2)
- Bottom Left (BL): (2, 2)

And a point (3, 3) to check:

1. Draw a Ray:
   - Draw a horizontal ray from (3, 3) to the right.

2. Count Intersections:
   - The ray intersects the edge (4, 4)-(4, 2) once.

3. Determine Inside or Outside:
   - The number of intersections is 1 (odd), so the point (3, 3) is inside the quadrilateral.

