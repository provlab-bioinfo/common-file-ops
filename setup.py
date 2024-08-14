from setuptools import setup, find_packages

setup(
    name='common_file_ops',
    version='0.1.0-alpha',
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'pip',
        'numpy',
        'pandas',
        'setuptools',
        "search_tools"
    ],
    python_requires='>=3.10, <4',
    description='A library of common file maniputation commands for various projects at APL.',
    url='https://github.com/provlab-bioinfo/common-file-ops',
    author='Andrew Lindsay',
    author_email='andrew.lindsay@albertaprecisionlabs.ca',
    include_package_data=True,
    keywords=[],
    zip_safe=False
)