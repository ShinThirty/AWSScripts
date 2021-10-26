venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt
format: venv/bin/activate
	./venv/bin/isort .
	./venv/bin/black .
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf venv
