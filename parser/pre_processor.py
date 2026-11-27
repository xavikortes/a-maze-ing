#!/usr/bin/env python3
"""Pre-processor for reading KEY=VALUE configuration files."""


def pre_processor(filepath: str) -> dict[str, str]:
    """Read a KEY=VALUE config file and return a cleaned dictionary.

    Args:
        filepath: Path to the configuration text file.

    Returns:
        A dictionary mapping configuration keys
        to raw string values.

    Raises:
        ValueError: If a line lacks '=', has an empty key,
        or has a duplicate key.
    """

    result: dict[str, str] = {}
    with open(filepath, 'r', encoding="utf-8") as file:

        for num_line, line in enumerate(file, start=1):
            clean_line = line.split("#", 1)[0].strip()

            if clean_line == "":
                continue
            if "=" not in clean_line:
                raise ValueError(
                    f"Syntax Error: in line {num_line}, missing '='"
                )

            key, value = clean_line.split("=", 1)
            key = key.strip()
            value = value.strip()

            if key == "" or key in result:
                raise ValueError(
                    f"Error: {key} in line {num_line} repeat or non exists."
                )

            result[key] = value

    return result
