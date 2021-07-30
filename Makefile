all: install

install:
	pip3 install -r requirements.txt

install-dev:
	pip3 install -e .
	pip3 install -r requirements-dev.txt

pre-commit:
	pre-commit run --all-files

test:
	pytest tests/tests.py