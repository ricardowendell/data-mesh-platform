.PHONY: all clean lint type test test-cov

CMD:=poetry run
PYMODULE:=dmp
TESTS:=tests

all: test lint

lint:
	$(CMD) flake8 $(PYMODULE) $(TESTS)

test:
	$(CMD) pytest $(TESTS)

test-cov:
	$(CMD) pytest --cov=$(PYMODULE) $(TESTS)

isort:
	$(CMD) isort --recursive $(PYMODULE) $(TESTS)

clean:
	git clean -Xdf # Delete all files in .gitignore