"""
circle.py
A demo project for APS Hack Day 2019

Handles the primary functions
"""

import numpy as np
from numpy import pi as π

class Circle:
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """
    def __init__(self, radius=1):
        self.radius = radius


    def __str__(self):
        return f"Circle(radius={self.radius})"
    
    @property
    def area(self):
        return π * (self.radius ** 2)

    # @property
    # def circumference(self):
    #     return 2* π * self.radius


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(Circle(5).area)
