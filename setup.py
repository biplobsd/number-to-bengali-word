from setuptools import setup

def readme():
    with open('README.md', 'r', encoding = 'utf-8') as f:
        README = f.read()
    return README


setup(
    name="Number-to-bengali-word",
    version="1.0",
    description="number-to-bengali-word",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/banglakit/number-to-bengali-word",
    author="banglakit",
    author_email="banglakit",
    license="Apache 2.0",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["number_to_bengali"],
    include_package_data=True,
    keywords=('bengali', 'bangla', 'number', 'word')
)
