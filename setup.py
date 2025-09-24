
from setuptools import setup, find_packages

setup(
    # Basic info
    name="students_performance",                     # Name of your package (should be unique on PyPI)
    version="0.1.0",                      # Follow semantic versioning (major.minor.patch)
    description="Performance Analysis of Students",
    long_description=open("README.md", "r", encoding="utf-8").read(),  # Full description
    long_description_content_type="text/markdown",  # Format of README
    
    # Author details
    author="Nimisha",
    author_email="nimisha121@gmail.com",
    url="https://github.com/nimmy2000/students_performance.git",  # Project homepage/repo
    
    # License
    license="MIT",                        # Choose license (MIT, Apache-2.0, GPL, etc.)
    
    # Find all sub-packages automatically
    packages=find_packages(),             # Or list manually: ["mathutils"]
    include_package_data=True,            # Include files specified in MANIFEST.in
    
    # Dependencies
    install_requires=[                     # Packages required for this to run
        # "numpy>=1.20.0",                # Example
    ]
)