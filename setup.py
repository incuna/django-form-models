from setuptools import setup, find_packages

setup(
    name = 'django-form-models',
    packages = find_packages(),
    include_package_data=True,
    install_requires=[
        'django-orderable>=1.0.1',
        'django-appconf>=0.5',
    ],
    version = '0.1.1',
    description = 'Sample models for modelling django forms and fields, and integrate with crispy forms layout.',
    author = 'Incuna Ltd',
    author_email = 'admin@incuna.com',
    url = 'http://incuna.com/',
)
