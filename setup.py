import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bted",
    version="0.0.6",
    author="Andrew Bihl",
    author_email="andrewbihlva@gmail.com",
    description="A simple syntax for text editing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andrewbihl/bted",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'bted = bted.interpreter:main'
        ]
    },
    include_package_data=True
)