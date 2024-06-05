def validate_radius(radius):
    """
    Validate the radius value.

    Parameters:
    radius (float): The radius of the sphere.

    Returns:
    bool: True if valid, raises ValueError if invalid.
    """
    if radius < 0:
        raise ValueError("The radius cannot be negative")
    return True
