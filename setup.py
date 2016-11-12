import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
PROJECT_NAME = 'django-simple-forum'

data_files = []
for dirpath, dirnames, filenames in os.walk(PROJECT_NAME):
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'):
            del dirnames[i]
    if '__init__.py' in filenames:
        continue
    elif filenames:
        for f in filenames:
            data_files.append(os.path.join(
                dirpath[len(PROJECT_NAME) + 1:], f))

setup(
    name='django-simple-forum',
    version='0.0.2',
    packages=['django_simple_forum', 'django_simple_forum.templatetags', 'django_simple_forum.migrations'],
    include_package_data=True,
    description='A Full featured forum, easy to integrate and use.',
    long_description=README,
    url='https://github.com/MicroPyramid/django-simple-forum',
    author='Micropyramid',
    author_email='hello@micropyramid.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        "Django>=1.6.0,<1.10",
        'django-simple-pagination',
        'django-storages',
        'microurl',
        'boto',
        'sendgrid',
        'sorl-thumbnail==12.4a1',
        'django-ses-gateway'
    ],
)
