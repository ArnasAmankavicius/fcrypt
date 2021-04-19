from setuptools import setup, find_packages

setup(
    name="fcrypt",
    author="Arnas Amankavicius",
    author_email="https://github.com/pradeepsen99",
    maintainer="Arnas Amankavicius",
    maintainer_email="https://github.com/ArnasAmankavicius",
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
    entry_points={"console_scripts": ["fcrypt=src.fcrypt:exec"]},
    install_requires=[
        "click>=7.1.2,<8.0.0",
        "cryptography>=3.4.7,<4.0.0"
    ]
)