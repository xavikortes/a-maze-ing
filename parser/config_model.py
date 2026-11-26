#!/usr/bin/env python3
"""Configuration data model and validation rules for the maze generator."""
from typing import Any

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
    ValidationError,
    model_validator
)


class MazeConfig(BaseModel):
    """Validated configuration model for the maze generator."""
    model_config = ConfigDict(extra="forbid", frozen=True)

    WIDTH: int = Field(..., gt=0)
    HEIGHT: int = Field(..., gt=0)
    ENTRY: tuple[int, int]
    EXIT: tuple[int, int]
    OUTPUT_FILE: str = Field(..., min_length=1)
    PERFECT: bool
    SEED: int | None = None

    @field_validator("ENTRY", "EXIT", mode="before")
    @classmethod
    def parse_coords(cls, value: Any) -> Any:
        """Split comma-separated coordinate strings into a 2-element tuple."""
        if isinstance(value, str):
            parts = value.split(",")

            if len(parts) != 2:
                raise ValueError("Invalid coordinate format, expected 'x,y'")

            return (parts[0].strip(), parts[1].strip())
        return value

    @model_validator(mode="after")
    def validate_maze_rules(self) -> "MazeConfig":
        """Validate cross-field maze constraints and boundaries."""
        entry_x, entry_y = self.ENTRY
        exit_x, exit_y = self.EXIT

        if not (0 <= entry_x < self.WIDTH and 0 <= entry_y < self.HEIGHT):
            raise ValueError("ENTRY coordinates are out of bounds!")
        if not (0 <= exit_x < self.WIDTH and 0 <= exit_y < self.HEIGHT):
            raise ValueError("EXIT coordinates are out of bounds!")

        if self.ENTRY == self.EXIT:
            raise ValueError("ENTRY and EXIT coordinates must be different")

        if not self.OUTPUT_FILE.strip():
            raise ValueError("OUTPUT_FILE cannot be empty or whitespace")

        return self


if __name__ == "__main__":
    valid_data: dict[str, Any] = {
        "WIDTH": "20",
        "HEIGHT": "15",
        "ENTRY": "0, 0",
        "EXIT": "19, 14",
        "OUTPUT_FILE": "maze.txt",
        "PERFECT": "True",
        "SEED": "42",
    }

    try:
        config = MazeConfig(**valid_data)
        print("--- CONFIGURACIÓN VÁLIDA ---")
        print(repr(config))
        print(f"Tipo de WIDTH: {type(config.WIDTH)}")
        print(f"Tipo de ENTRY: {type(config.ENTRY)} -> {config.ENTRY}")
    except ValidationError as err:
        print(err)

    invalid_data: dict[str, Any] = {
        "WIDTH": "-5",
        "HEIGHT": "15",
        "ENTRY": "0,0,9",
        "EXIT": "19,14",
        "OUTPUT_FILE": "maze.txt",
        "PERFECT": "True",
        "CLAVE_INVENTADA": "123",
    }

    try:
        MazeConfig(**invalid_data)
    except ValidationError as err:
        print("\n--- ERRORES DETECTADOS POR PYDANTIC ---")
        print(err)

    invalid_bounds_data: dict[str, Any] = {
        "WIDTH": "20",
        "HEIGHT": "15",
        "ENTRY": "0, 0",
        "EXIT": "20, 15",
        "OUTPUT_FILE": "maze.txt",
        "PERFECT": "True",
    }

    try:
        MazeConfig(**invalid_bounds_data)
    except ValidationError as err:
        print("\n--- ERROR DE REGLAS ESPACIALES (FASE 3) ---")
        print(err)
