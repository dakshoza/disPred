from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'An Integrated Real-Time Wheat and Tomato Disease Detection System'

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Setting up
setup(
    name="disPred",
    version=VERSION,
    author="dakshoza (Daksh Oza)",
    author_email="<ozadaksh31@gmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['opencv-python==4.8.0.74', 'numpy==1.23.5', 'tensorflow==2.14.0'],
    keywords=['crop detection', 'tensorflow lite', 'wheat', 'tomato', 'real time'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Agriculture",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',  
    include_package_data=True,
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/disPred/issues",
        "Source Code": "https://github.com/yourusername/disPred",
    },
)