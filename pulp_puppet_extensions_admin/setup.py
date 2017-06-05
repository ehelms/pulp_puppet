from setuptools import setup, find_packages

requirements = [
    'pulp-puppet-common'
]

setup(
    name='pulp-puppet-cli',
    version='3.0.0a1.dev0',
    license='GPLv2+',
    packages=find_packages(exclude=['test', 'test.*']),
    author='Pulp Team',
    install_requires=requirements,
    author_email='pulp-list@redhat.com',
    description='pulp-cli extensions for the puppet plugin',
    entry_points={
        'pulp.extensions.admin': [
            'repo_admin = pulp_puppet.extensions.admin.pulp_cli:initialize',
        ]
    }
)
