NAME=a_maze_ing
CONFIG=config.txt

VENV=.venv

PY=$(VENV)/bin/python3
PDB=$(PY) -m pdb
PIP=$(PY) -m pip
FLAKE=$(PY) -m flake8
MYPY=$(PY) -m mypy

all: run

install: $(VENV)

run: $(VENV)
	$(PY) $(NAME).py $(CONFIG)

debug: $(VENV)
	$(PDB) $(NAME).py $(CONFIG)

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
# 	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

fclean: clean
	rm -rf $(VENV)

lint: $(VENV)
	$(FLAKE) . && $(MYPY) . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict: $(VENV)
	$(FLAKE) . && $(MYPY) . --strict

$(VENV): requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

.PHONY: all install run debug clean fclean lint lint-strict
