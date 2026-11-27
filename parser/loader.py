#!/usr/bin/env python3
"""Orchestrate configuration file loading, parsing, and validation."""
from pydantic import ValidationError
from parser.config_model import MazeConfig
from parser.pre_processor import pre_processor


class ConfigError(Exception):
    """Raised when configuration loading or validation fails."""


def parse_config(filepath: str) -> MazeConfig:
    """Load, pre-process, and validate a maze configuration file.

    Args:
        filepath: Path to the configuration text file.

    Returns:
        A validated and immutable MazeConfig instance.

    Raises:
        ConfigError: If the file cannot be read or contains invalid data.
    """
    try:
        dictionary = pre_processor(filepath)
        return MazeConfig.model_validate(dictionary)
    except OSError as e:
        raise ConfigError(f"Cannot read '{filepath}': {e}") from e
    except (ValueError, ValidationError) as e:
        raise ConfigError(
            f"Invalid configuration in '{filepath}': {e}"
        ) from e
