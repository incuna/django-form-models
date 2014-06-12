SHELL := '/bin/bash'

test:
	python form_models/tests/run.py

release:
	python setup.py register sdist upload
