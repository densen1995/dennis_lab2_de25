""""unit test for class cube"""
import pytest
from pytest import raises

import math
from cube import Cube

def test_valid_init():
    c1= Cube(side= 3)
    assert c1.side == (3)

def test_string_in_init_fails():
    """Test that initializing a cube with a string raises a TypeError."""
    with raises(TypeError):
        Cube(side="2")

def test_negative_value_in_init_fails():
   """Test that initializing a cube with a negative value raises a ValueError."""
   with raises(ValueError):
        Cube(side= -2)


def test_valid_cube_area_volume_and_perimeter():
    """Test the cube's surface area and volume calculations."""
    cube = Cube(side=2)
    assert cube.area == 24  
    assert cube.volume == 8 
    assert cube.perimeter ==  24 

def test_is_unit_cube():
    """Check if a cube correctly identifies as a unit cube."""
    c1 = Cube(side=1)
    c2 = Cube(side=3)
    assert c1.is_unit_cube() is True
    assert c2.is_unit_cube() is False
       

def test_cube_translation():
    """test trasnlating the cube in 3D."""
    cube=Cube(side=3)
    cube.translate(1,2,3)
    assert (cube._x, cube._y, cube._z) == (1,2,3)

def test_cube_comparison():
    """Test comparison operator overload for cubes"""
    c1=Cube(side=2)
    c2=Cube(side=3)

    assert c1 < c2
    assert c2 > c1
    assert not (c1 == c2)

def test_cube_equality():
    """testing two cubes with same side (should be equal)"""
    c1 = Cube(side=3)
    c2 = Cube(side=3)
    assert c1 == c2



