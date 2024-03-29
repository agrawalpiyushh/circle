"""
Unit and regression test for the circle package.
"""

# Import package, test suite, and other packages as needed
import circle
import pytest
import sys
import numpy as np
from numpy import pi as π

test_radius = 5

def test_circle_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "circle" in sys.modules

def test_circle_radius():
    test_radius = 5
    test_area = π * (test_radius**2)
    assert  test_area == circle.Circle(test_radius).area

def test_circle_circumference():
    test_radius = 5
    test_circumference = 2 * π * test_radius
    assert test_circumference == circle.Circle(test_radius).circumference

def test_circle__str__():
    test_radius = 5
    test__str__ = f"Circle(radius={test_radius})"
    assert test__str__ == str(circle.Circle(test_radius))