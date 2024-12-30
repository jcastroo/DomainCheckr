from setuptools import setup

setup(
    name='DomainCheckr',
    version='0.1',
    scripts=['whois_jcastroo.py'],
    install_requires=[
        'python-whois',
        'colorama',
    ],
    description='Checks the availability of domain names',
    author='João Castro',
    author_email='joaopedcastro@icloud.com',
    url='https://github.com/jcastroo/DomainCheckr',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
