# setup.py
from setuptools import setup, find_packages

setup(
    name="First_Package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["PyQt5"],
    description="Un paquete de ejemplo en Python con interfaz gráfica usando PyQt5",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Uriel Ruíz",
    author_email="Uriel_fisica@ciancias.unam.mx",
    url="https://github.com/Thunderbird2rj/TSFC3.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'First_Package_gui = First_Package.gui:main',
        ],
    },
)
