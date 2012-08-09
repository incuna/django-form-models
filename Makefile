SHELL := '/bin/bash'

test:
	django-admin.py test --settings=tests.settings

release:
	python setup.py register sdist upload
