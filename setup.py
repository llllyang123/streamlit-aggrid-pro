import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="streamlit-aggrid-pro",
    version="0.2.30",
    author="Pablo Fonseca",
    author_email="yangxiaochuang2@163.com",
    description="Streamlit component implementation of ag-grid-pro",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PablocFonseca/streamlit-aggrid",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[
        "streamlit >= 0.75",
        "simplejson >= 3.0",
        "pandas",
        "numpy"
    ]
)