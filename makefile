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
	PYTHONPATH=scripts venv/bin/python -m unittest discover -s tests -v

run:
	PYTHONPATH=scripts venv/bin/python scripts/vct21_stats_script.py

analyze:
	
	PYTHONPATH=scripts venv/bin/python scripts/generate_md.py

	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		git add images/plot.png Data_summary.md; \
		git commit -m "Add generated plot and report"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi
