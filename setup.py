from setuptools import setup, find_packages

setup(
    name="jetSDR: jetson-ai-specialist",
    version="0.1.0",
    description="Jetson Ai Specialist project: jetsonSDR.",
    author="Michael Nau",
    author_email="michaelwnau@gmail.com",
    packages=find_packages(),  # Automatically find and include all packages in the directory
    install_requires=[
        # List project dependencies here
        # e.g., 'numpy>=1.18.0', 'requests>=2.24.0'
    ],
    extras_require={
        "dev": [
            # List development dependencies here
            # e.g., 'pytest>=6.2.2', 'black'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
