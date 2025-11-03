import pytest
from pytest import raises

import math

from sphere import Sphere

def test_string_in_init_fails():
    with raises (TypeError):
         Sphere("2")

"""decorator function that allows me run both value and type error"""
@pytest.mark.parametrize("radius, expected_exception", [
    (-2, ValueError),  
    ("Dennis", TypeError), 
])

def test_sphere_invalid_inputs(radius, expected_exception):
    """test that invalid radius values raise the correct exceptions"""
    print(f"\nTesting invalid radius input: {radius}")
    with raises(expected_exception):
        Sphere(radius= radius)

         

    

def test_sphere_area_and_volume():
    """Test surface area and volume of a sphere."""
    sphere = Sphere(radius=1)
    assert round(sphere.area, 2) == round(4 * math.pi * 1**2, 2)
    assert round(sphere.volume, 2) == round((4/3) * math.pi * 1**3, 2)


def test_sphere_translation():
    """Test moving the sphere in 3D space."""
    sphere = Sphere(radius=2)
    sphere.translate(2, 3, 4)
    assert (sphere._x, sphere._y, sphere._z) == (2, 3, 4)


def test_sphere_comparisons():
    """Test comparison operators for spheres."""
    s1 = Sphere(radius=1)
    s2 = Sphere(radius=2)
    assert s1 < s2
    assert s2 > s1
    assert not (s1 == s2)




