SHELL := '/bin/bash'

test:
	django-admin.py test --settings=tests.settings
