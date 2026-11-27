#!/usr/bin/env python3
"""2D maze grid representation, wall manipulation, and rendering."""
from maze.walls import DELTA_TO_WALLS, Wall


"""
7x5 bitmap offsets forming the '42' pattern centered in the maze:

    #·#·###
    #·#···#
    ###·###
    ··#·#··
    ··#·###
"""
PATTERN_42: tuple[tuple[int, int], ...] = (
    (0, 0), (2, 0), (4, 0), (5, 0), (6, 0),
    (0, 1), (2, 1), (6, 1),
    (0, 2), (1, 2), (2, 2), (4, 2), (5, 2), (6, 2),
    (2, 3), (4, 3),
    (2, 4), (4, 4), (5, 4), (6, 4),
)


class Maze:
    """Represent a 2D maze grid with wall bitmasks and blocked cells."""
    def __init__(
        self,
        width: int,
        height: int,
        entry: tuple[int, int],
        exit_pos: tuple[int, int]
    ) -> None:
        """Initialize a closed maze grid of size width x height.

        Args:
            width: Number of columns in the maze (must be > 0).
            height: Number of rows in the maze (must be > 0).
            entry: Coordinates (x, y) of the maze entrance.
            exit_pos: Coordinates (x, y) of the maze exit.

        Raises:
            ValueError: If width or height is less than or equal to zero.
        """

        if width <= 0 or height <= 0:
            raise ValueError("Maze dimensions must be positive")

        self.width = width
        self.height = height
        self.entry = entry
        self.exit_pos = exit_pos
        self.grid: list[
            list[Wall]
        ] = [
            [Wall.ALL for _ in range(width)]
            for _ in range(height)
        ]
        self.blocked: set[tuple[int, int]] = set()

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if (x, y) lies inside the grid boundaries."""
        return 0 <= x < self.width and 0 <= y < self.height

    def has_wall(self, x: int, y: int, wall: Wall) -> bool:
        """Return True if the specified wall is present at cell (x, y).

        Raises:
            ValueError: If (x, y) is outside the grid boundaries.
        """
        if not self.in_bounds(x, y):
            raise ValueError("Coordinates out of bounds")
        return bool(self.grid[y][x] & wall)

    def remove_wall(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """Remove the shared wall between two orthogonally adjacent cells.

        Raises:
            ValueError: If coordinates are out of bounds, refer to blocked
                cells, or are not orthogonally adjacent.
        """
        if not self.in_bounds(x1, y1) or not self.in_bounds(x2, y2):
            raise ValueError("Coordinates out of bounds")

        if (x1, y1) in self.blocked or (x2, y2) in self.blocked:
            raise ValueError("Cannot remove walls of blocked cells")

        delta = (x2 - x1, y2 - y1)
        if delta not in DELTA_TO_WALLS:
            raise ValueError("Cells are not orthogonally adjacent")

        wall_1, wall_2 = DELTA_TO_WALLS[delta]
        self.grid[y1][x1] &= ~wall_1
        self.grid[y2][x2] &= ~wall_2

    def stamp_42(self) -> bool:
        """Stamp the centered 7x5 '42' pattern into blocked cells.

        Requires a minimum grid size of 11x9 and ensures neither entry nor
        exit overlaps with the pattern cells.

        Returns:
            True if the pattern was stamped; False if skipped.
        """
        if self.width < 11 or self.height < 9:
            return False

        start_x = (self.width - 7) // 2
        start_y = (self.height - 5) // 2
        cells = {(start_x + dx, start_y + dy) for dx, dy in PATTERN_42}

        if self.entry in cells or self.exit_pos in cells:
            return False
        self.blocked.update(cells)
        for x, y in cells:
            self.grid[y][x] = Wall.ALL
        return True

    def to_hex_rows(self) -> list[str]:
        """Return maze rows encoded as uppercase hexadecimal strings."""
        return [
            "".join(format(int(cell), "X") for cell in row)
            for row in self.grid
        ]

    def render_ascii(self, path: set[tuple[int, int]] | None = None) -> str:
        """Render the maze grid as an ASCII string for terminal display.

        Args:
            path: Optional set of (x, y) coordinates to mark as the solution
                route.

        Returns:
            Multiline string representing walls, entry, exit, and blocked
            cells.
        """
        lines: list[str] = []

        for y in range(self.height):
            top = "+"
            for x in range(self.width):
                if self.has_wall(x, y, Wall.NORTH):
                    top += "---+"
                else:
                    top += "   +"
            lines.append(top)

            mid = ""
            for x in range(self.width):
                if self.has_wall(x, y, Wall.WEST):
                    mid += "|"
                else:
                    mid += " "

                if (x, y) == self.entry:
                    mid += " E "
                elif (x, y) == self.exit_pos:
                    mid += " X "
                elif (x, y) in self.blocked:
                    mid += "###"
                elif path is not None and (x, y) in path:
                    mid += " · "
                else:
                    mid += "   "

            if self.has_wall(self.width - 1, y, Wall.EAST):
                mid += "|"
            else:
                mid += " "
            lines.append(mid)

        bottom = "+"
        for x in range(self.width):
            if self.has_wall(x, self.height - 1, Wall.SOUTH):
                bottom += "---+"
            else:
                bottom += "   +"
        lines.append(bottom)

        return "\n".join(lines)
