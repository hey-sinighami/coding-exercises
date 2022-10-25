import math


def area_square(l):
    if l < 0:
        raise ValueError(f'Invalid input: Length: {l}')

    return l * l

def area_rectangle(l, w):
    if l < 0 or w < 0:
        raise ValueError(f'Invalid input: Length: {l}, Width: {w}')

    return l * w

def surface_area_cube(l):
    if l < 0:
        raise ValueError(f'Invalid input: Length: {l}')

    return 6 * l **2

def surface_area_cuboid(l, w, h):
    if l < 0 or w < 0 or h < 0:
        raise ValueError(f'Invalid input: Length: {l}, Width: {w}, Height: {h}')

    return 2 * ((l* w) + (w * h) + (l * h))

def surface_area_sphere(radius):
    if radius < 0:
        raise ValueError(f'Invalid radius: {radius}')

    return 4 * math.pi * radius**2

assert(area_rectangle(3, 5) == 15)
assert(area_square(8) == 64)
assert(surface_area_cube(17) == 1734)
assert(surface_area_cuboid(3, 5, 7) == 142)
assert(surface_area_sphere(32) == 12867.963509103793)
