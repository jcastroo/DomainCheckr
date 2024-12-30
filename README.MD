# DomainCheckr

**DomainCheckr** is a simple and effective tool that allows you to check the availability of domain names on the internet. This script supports several popular extensions, such as `.com`, `.net`, `.org`, and others.

## Functionality

The main functionality of **DomainCheckr** is to allow the user to check if a specific domain is available for registration. It tries to register the domain with several popular extensions and displays whether the domain is available or already taken.

## Installation

### 1. Clone the repository

Clone the GitHub repository with the following command:
git clone https://github.com/jcastroo/DomainCheckr.git


### 2. Navigate to the repository folder

After cloning, enter the repository folder:
cd DomainCheckr


### 3. Install the dependencies

Install the dependencies with the command:
pip install .


> **Note**: Make sure you have Python 3.x installed.

## Usage

After installing **DomainCheckr**, you can use the `domaincheckr` command directly from the command line to check the availability of a domain.

### Syntax
domaincheckr <domain>


Where `<domain>` is the domain name you want to check (without the extension).

### Example

If you want to check the availability of the domain `example`, run the following command:
domaincheckr example


The script will check the following extensions: `.com`, `.net`, `.org`, `.info`, `.co`, `.io` and show if the domain is available or already registered.

### Result

**DomainCheckr** will display available domains in green and already registered domains in red.

## Contribution

If you want to contribute to **DomainCheckr**, feel free to open *issues* or *pull requests*.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Author

- **João Castro** - [@jcastroo](https://github.com/jcastroo)





