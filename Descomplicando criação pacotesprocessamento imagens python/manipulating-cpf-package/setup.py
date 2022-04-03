from setuptools import setup, find_packages

with open("README.md", "r") as f:
	page_description = f.read()

with open("requirements.txt") as f:
	requirements = f.read().splitlines()

setup(
	name="manipulating-cpf-package",
	version="0.0.1",
	author="George",
	author_email="george.apolonio@hotmail.com",
	url="https://github.com/GeorgeApolonio/ManipularCPF.git",
	description="gerador e validador de cpf",
	long_description=page_description,
	long_description_content_type="text/markdown",
	packages=find_packages(),
	install_requires=["wheel", "bar", "greek"],
)