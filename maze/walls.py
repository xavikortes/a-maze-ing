#!/usr/bin/env python3
"""Bitmask definitions and directional helpers for maze cell walls."""
from enum import IntFlag


class Wall(IntFlag):
    """Bitmask flags representing closed walls around a cell."""
    NONE = 0
    NORTH = 1 << 0
    EAST = 1 << 1
    SOUTH = 1 << 2
    WEST = 1 << 3
    ALL = NORTH | EAST | SOUTH | WEST


DELTA_TO_WALLS: dict[tuple[int, int], tuple[Wall, Wall]] = {
    (0, -1): (Wall.NORTH, Wall.SOUTH),
    (1, 0): (Wall.EAST, Wall.WEST),
    (0, 1): (Wall.SOUTH, Wall.NORTH),
    (-1, 0): (Wall.WEST, Wall.EAST)
}


WALL_TO_DELTA: dict[Wall, tuple[int, int]] = {
    Wall.NORTH: (0, -1),
    Wall.EAST: (1, 0),
    Wall.SOUTH: (0, 1),
    Wall.WEST: (-1, 0)
}


WALL_TO_CHAR: dict[Wall, str] = {
    Wall.NORTH: "N",
    Wall.EAST: "E",
    Wall.SOUTH: "S",
    Wall.WEST: "W"
}
