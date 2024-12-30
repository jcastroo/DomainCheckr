from setuptools import setup

setup(
    name='DomainCheckr',
    version='0.1',
    scripts=['domaincheckr.py'],  
    install_requires=[
        'python-whois',
        'colorama',
    ],
    description='Checks the availability of domain names with a unique touch by jcastroo.',
    author='João Castro',
    author_email='seu_email@example.com',
    url='https://github.com/jcastroo/DomainCheckr',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'console_scripts': [
            'domaincheckr=domaincheckr:main', 
        ],
    },
)
