import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="roll-dice",
    version="0.0.1",
    author="Marija Kalebota Kodzoman",
    author_email="marija.kalebota@gmail.com",
    description="A dice-rolling application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    #python_requires='>=3.6',
)
