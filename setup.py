import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easydbio",
    version="0.3.2",
    author="JakeCooper",
    author_email="jake.elijah.cooper@gmail.com",
    description="Python module for EasyDB.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EasyDB-io/Python-Client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
