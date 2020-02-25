venv:
	virtualenv --python=python3.6 venv
	venv/bin/pip install -r requirements.txt

test: venv
	venv/bin/python bloom_filter_test.py
