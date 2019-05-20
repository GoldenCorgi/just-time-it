import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="just-time-it",
    version="0.0.1",
    author="GoldenCorgi",
    description="The fuss-free way to time functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GoldenCorgi/just-time-it",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ],
)
