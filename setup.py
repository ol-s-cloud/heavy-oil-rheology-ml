from setuptools import setup, find_packages

setup(
    name="aurelia",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
    ],
    extras_require={
        'dev': ['pytest', 'mypy'],
        'research': ['torch', 'shap'],
        'enterprise': ['tensorflow', 'kubernetes']
    },
    author="Aurelia Research Team",
    description="Advanced Scientific Machine Learning Framework",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ol-s-cloud/heavy-oil-rheology-ml",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ]
)