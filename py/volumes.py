from math import pi, pow

def vol_cube(l):
    if l < 0:
        raise ValueError(f'Invalid input: Length: {l}')

    return pow(l, 3)

def vol_prism(a_b, h):
    if a_b < 0 or h < 0:
        raise ValueError(f'Invalid input: Area of Base: {b}, Height: {h}')

    return float(a_b * h)

def vol_pyramid(b, h):
    if b < 0 or h < 0:
        raise ValueError(f'Invalid input: Base: {b}, Height: {h}')

    return b * h / 3.0

def vol_sphere(r):
    if r < 0:
        raise ValueError(f'Invalid input: Radius: {r}')

    return 4 / 3 * pi * pow(r, 3)


assert(vol_cube(13) == 2197)
assert(vol_prism(11, 34) == 374)
assert(vol_pyramid(12, 8) == 32)
assert(vol_sphere(7) == 1436.7550402417319)

