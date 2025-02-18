from setuptools import setup, find_packages

setup(
    name='heavy_oil_ml',
    version='0.1.0',
    description='Machine learning pipeline for analyzing heavy oil rheological properties',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Falade, A.A., Sa\'id, O., Akinsete, O.O',
    author_email='research.contact@example.com',
    url='https://github.com/ol-s-cloud/heavy-oil-rheology-ml',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'scikit-learn',
        'shap'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Physics'
    ],
    keywords='machine-learning petroleum-engineering rheology data-science',
    python_requires='>=3.8',
)