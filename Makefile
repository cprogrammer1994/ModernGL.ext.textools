ifeq ($(OS), Windows_NT)
	PYTHON = python
else
	PYTHON = python3
endif

all:
	$(PYTHON) -m pip install -U .

wheel:
	$(PYTHON) setup.py bdist_wheel --universal

docs:
	$(PYTHON) setup.py build_sphinx

.PHONY: all wheel docs
