#!/usr/bin/env python3
"""Public interface for the maze configuration parser."""
from parser.loader import ConfigError, parse_config
from parser.config_model import MazeConfig


__all__ = [
    "MazeConfig",
    "ConfigError",
    "parse_config"
]
