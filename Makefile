NAME=a_maze_ing

PY=python3
PDB=$(PY) -m pdb

VENV=.venv

PIP=$(VENV)/bin/pip
FLAKE=$(VENV)/bin/flake8
MYPY=$(VENV)/bin/mypy

all: run

install: $(VENV)

run: $(VENV)
	$(PY) $(NAME).py

debug: $(VENV)
	$(PDB) $(NAME).py

clean:
	rm -rf $(VENV)
	find . -type d -name __pycache__ -delete
	find . -type d -name .mypy_cache -delete
# 	find . -type f -name *.pyc -delete

lint: $(VENV)
	$(FLAKE) . && $(MYPY) . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict: $(VENV)
	$(FLAKE) . && $(MYPY) . --strict

$(VENV): requirements.txt
	$(PY) -m venv $(VENV)
	$(PIP) install -r requirements.txt
	touch $(VENV)

.PHONY: all install run debug clean lint lint-strict
