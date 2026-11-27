#!/usr/bin/env python3
"""Public interface for the maze grid and wall bitmasks."""
from maze.grid import Maze, PATTERN_42
from maze.walls import DELTA_TO_WALLS, WALL_TO_CHAR, WALL_TO_DELTA, Wall


__all__ = [
    "Maze",
    "PATTERN_42",
    "Wall",
    "DELTA_TO_WALLS",
    "WALL_TO_DELTA",
    "WALL_TO_CHAR",
]
