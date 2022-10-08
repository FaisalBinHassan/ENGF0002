# ----------------------------------------------------------------
# Algorithm:

# 1- Circle and sqaure points (initialise with 0 ) ==> used to count number of points in it
# 2- To perform if points are in circle, generate random x and y to do this equation ( x^2 + y^2 <= 1 ) => +circle_points
# 3- then increment square points
# 4- go over the +(numOfDarts_Thrown)
# 5- with the formal equation of [ pie / 4 = Nhits(circle) / Ntotalhits(square) ] == [ pie = 4 * ( Nhits / Ntotalhits) ]

# ----------------------------------------------------------------

import random

def estimate_pi_d(precision):
    # Points got into the circle and square
    circle_points = 0
    square_points = 0

    # Total Random numbers generated = possible x values* possible y values
    for i in range(precision):

        # Randomly generated x and y values from a
        # uniform distribution
        # Range of x and y values is 0 to 1
        rand_x = random.uniform(0, 1)
        rand_y = random.uniform(0, 1)

        # Distance between (x, y) from the origin
        origin_dist = rand_x ** 2 + rand_y ** 2

        # Checking if (x, y) lies inside the circle
        if origin_dist <= 1:
            circle_points += 1

        square_points += 1

        # Estimating value of pi,
        # pi= 4*(no. of points generated inside the
        # circle)/ (no. of points generated inside the square)
        pi = 4 * circle_points / square_points

    ##    print(rand_x, rand_y, circle_points, square_points, "-", pi)
    # print("\n")

    print("Final Estimation of Pi=", pi)


# To find number of points that are inside the square and in-between the circle,
# we'd have to initiate number of darts thrown (example)
numOfDarts_Thrown = 1000000

estimate_pi_d(numOfDarts_Thrown)


