from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="my-awesome-library",
    version="0.1.0",
    author="Maria Dancianu",
    author_email="mariadanci1994@gmail.com,
    description="My first Python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my-awesome-library",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[
        # Add any dependencies here
        # "requests>=2.25.0",
    ],
)