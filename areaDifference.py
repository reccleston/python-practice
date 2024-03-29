# https://edabit.com/challenge/NNhkGocuPMcryW7GP
#
# Imagine a circle and two squares: a smaller and a bigger one. For 
# the smaller one, the circle is a circumcircle and for the bigger one, an incircle.
#
# Create a function, that takes an integer (radius of the circle) 
# and returns the difference of the areas of the two squares.

def areaDifference(radius):
    radius = float(radius)
    radius_sqaured = radius ** 2
    # area diff = lrg sq - sm sq
        # lrg sq area --> 4r^2
        # sm sq area --> 2r^2
        # diff is 4r^2 - 2r^2 = 2r^2

    return f'The difference in area of an incircle and circumscribed circle is {2 * radius_sqaured}'

print(areaDifference(input()))