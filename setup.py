from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_basics",
    version="0.0.1",
    author="Carrascosa, Alexandre",
    author_email="alexandrecarrascosa@gmail.com",
    description="Personal package to process image",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlexandreCarrascosa/image-basics-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)