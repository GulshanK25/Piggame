PYTHON :=
ifeq ($(OS),Windows_NT)
	PYTHON=.venv\Scripts\python
else
	PYTHON=.venv/bin/python
endif

venv:
	test -d .venv || python3 -m venv .venv/
	. .venv/Scripts/activate

install-requirements: check-venv
	$(PYTHON) -m pip install --upgrade -q pip
	$(PYTHON) -m pip install -r requirements.txt

install-toml: check-venv
	$(PYTHON) -m pip install --upgrade -q pip
	$(PYTHON) -m pip install .

## creates dist files and package release files based on pyproject.toml (depends on check-virtual-env)
build-toml: install-toml
	$(PYTHON) -m pip install --upgrade -q pip
	$(PYTHON) -m build

run: check-venv
	@$(PYTHON) main.py

check-venv:
	@if [ -z "$$(which python | grep -o .venv)" ]; then \
		exit 1; \
	fi

pylint: check-venv
	@find src/ -name '*.py' -print0 | xargs -0 pylint -d C0103 -rn

test: check-venv
	$(PYTHON) -m unittest discover -p 'test_*.py' -v -b

flake8: check-venv
	@$(call MESSAGE,$@)
	@-flake8 --exclude=.svn,CVS,.bzr,.hg,.git,__pycache__,.tox,.nox,.eggs,*.egg,.venv,venv,*.pyc

clean:
	@$(call MESSAGE,$@)
	rm -f .coverage *.pyc
	rm -rf __pycache__
	rm -rf htmlcov

coverage:
	@$(call MESSAGE,$@)
	coverage run -m unittest discover
	coverage html
	coverage report -m

