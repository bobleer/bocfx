import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bocfx",
    version="0.6.6",
    author="bobleer",
    author_email="liwenbo628@gmail.com",
    description="Easy way to get foreign exchange rate from Bank of China.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bobleer/bocfx",
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': [
            'bocfx = bocfx:asexec',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)