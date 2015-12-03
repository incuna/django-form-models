SHELL := '/bin/bash'

test:
	coverage run form_models/tests/run.py
	coverage report

release:
	python setup.py register sdist upload
