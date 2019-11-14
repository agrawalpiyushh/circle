"""
Unit and regression test for the circle package.
"""

# Import package, test suite, and other packages as needed
import circle
import pytest
import sys

def test_circle_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "circle" in sys.modules
