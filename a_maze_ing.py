#!/usr/bin/env python3
"""Entry point for the A-Maze-Ing maze generator application."""
import sys
from parser import ConfigError, parse_config


def main() -> None:
    """Parse command-line arguments and load the maze configuration.

    Reads the configuration file path from sys.argv, validates it using
    parse_config, and exits with status code 1 on usage or config errors.
    """

    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py <config_file>", file=sys.stderr)
        sys.exit(1)

    try:
        config = parse_config(sys.argv[1])
    except ConfigError as err:
        print(err, file=sys.stderr)
        sys.exit(1)

    print(config)


if __name__ == "__main__":
    main()
