# Planar-MIS
Planar Maximal Independent Sets

### Setup

Create a Python virtualenv with interpreter version 2.7 or later on your UNIX system. Activate the virtualenv with `source bin/activate`, and then create a new folder called `project`. Navigate into this folder, and clone this repository.

### Dependency Installation

Cython is required for this project. In order to ensure that it is installed before the remaining dependencies, run `pip install --upgrade git+git://github.com/cython/cython@master`. Then, if you are on a Linux system, you may need to run `apt-get install libfreetype6-dev python-dev tcl-dev tk-dev
 python-matplotlib`. Install all remaining dependencies by running `pip install -r requirements.txt`.  

### Output

All output should go to ./data until we find a better way to display our results.
