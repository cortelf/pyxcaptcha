import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyxcaptcha",
    version="0.1.0",
    author="CortelF",
    author_email="zdaw07@yahoo.com",
    description="Python API wrapper for x-captcha service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cortelf/pyxcaptcha",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)