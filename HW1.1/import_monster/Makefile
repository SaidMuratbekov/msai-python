PACKAGES="src"
REQUIREMENTS_DEV="requirements-dev.txt"
REQUIREMENTS="requirements.txt"


all: install black

check_all:
    @pre-commit run --all-files

pytest:
    @pytest

black:
	@black ${PACKAGES}

isort:
	@isort ${PACKAGES}

clean:
	@rm -rf `find . -name __pycache__`
	@rm -f `find . -type f -name '*.py[co]' `
	@rm -f `find . -type f -name '*~' `
	@rm -f `find . -type f -name '.*~' `
	@rm -f `find . -type f -name '@*' `
	@rm -f `find . -type f -name '#*#' `
	@rm -f `find . -type f -name '*.orig' `
	@rm -f `find . -type f -name '*.rej' `
	@rm -rf `find . -type d -name '.pytest_cache' `
	@rm -f .coverage
	@rm -rf htmlcov
	@rm -rf build
	@rm -rf cover
	@python setup.py clean
	@rm -rf .tox
	@rm -f .develop
	@rm -f .flake

install-dev:
	@pip install -r ${REQUIREMENTS_DEV}
	@pip install -e .

install:
	@pip install -r ${REQUIREMENTS}
	@pip install -e .

install-pre-commit: install-dev
	@pre-commit install

install-all: install-dev install-test

.PHONY: all install-dev uninstall clean test