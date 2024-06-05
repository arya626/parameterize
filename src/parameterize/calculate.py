import math


def volume(radius):
    """
    Calculate the volume of a sphere using the parameterization.

    Parameters:
    radius (float): The radius of the sphere.

    Returns:
    float: The volume of the sphere.
    """
    if radius < 0:
        raise ValueError("The radius cannot be negative")

    volume = (4 / 3) * math.pi * (radius ** 3)
    return volume
