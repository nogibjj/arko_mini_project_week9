venv:
	python -m venv venv

install: venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -r requirements.txt

format:
	venv/bin/black scripts/*.py tests/*.py

lint:
	venv/bin/pylint scripts/*.py tests/*.py
	

test:
	PYTHONPATH=src venv/bin/python -m unittest discover -s tests -v

run:
	PYTHONPATH=src venv/bin/python scripts/VCT21_stats_script.py
