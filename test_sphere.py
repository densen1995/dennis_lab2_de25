""""unit testing for class sphere"""
import pytest
from pytest import raises

import math

from sphere import Sphere
from cube import Cube

def test_valid_init():
    s1= Sphere(radius= 2)
    assert s1.radius == (2) 

def test_string_in_init_fails():
    """Test that initializing a sphere with a string raises a TypeError."""
    with raises(TypeError):
        Sphere(radius="Dennis")

def test_negative_value_in_init_fails():
   """Test that initializing a sphere with a negative value raises a ValueError."""
   with raises(ValueError):
        Sphere(radius = -2)


def test_valid_sphere_area_volume_and_circumference():
    """Test s area ,circumference and volume of a sphere."""
    sphere = Sphere(radius=1)
    assert round(sphere.area, 2) == round(4 * math.pi * 1**2, 2)
    assert round(sphere.volume, 2) == round((4/3) * math.pi * 1**3, 2)
    assert round(sphere.circumference, 2) == round (2 * math.pi ,2)

def test_is_unit_sphere():
    """Check if a sphere correctly identifies as a unit sphere."""
    s1 = Sphere(radius=1)
    s2 = Sphere(radius=3)
    assert s1.is_unit_sphere() is True
    assert s2.is_unit_sphere() is False


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

def test_sphere_equality():
    """testing two cubes with same radius (should be equal)."""
    s1 = Sphere(radius=4)
    s2 = Sphere(radius=4)
    assert s1 == s2

def test_cube_vs_sphere_comparisons():
    
    """Test comparing a Cube and a Sphere based on their  area ."""

    cube = Cube(side=2)       # Surface area = 24
    sphere = Sphere(radius=2) # Surface area = 50.27

    """Since 24 < 50.27, cube should be considered smaller"""
    assert cube < sphere
    assert sphere > cube
    assert not cube == sphere

    """Change comparison mode to volume and compare again"""
    cube.compare_by = "volume"
    sphere.compare_by = "volume"

    """Cube volume = 8, Sphere volume = 33.51"""
    assert cube < sphere
    assert sphere > cube


def test_sphere_repr_output():
    """ensure Sphere.__repr__() returns a readable string """
    sphere = Sphere(x=1, y=2, z=3, radius=3)
    output=repr(sphere)
    assert "Sphere" in output
    assert "radius = 3"





