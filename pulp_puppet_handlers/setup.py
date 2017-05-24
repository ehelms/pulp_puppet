from setuptools import setup, find_packages

setup(
    name='pulp_puppet_handlers',
    version='2.13.2a1',
    license='GPLv2+',
    packages=find_packages(exclude=['test', 'test.*']),
    author='Pulp Team',
    author_email='pulp-list@redhat.com',
)
