# Parameterization Package

This package computes the volume of a sphere given its radius. The **src** directory is organized into three subdirectories: examples, tests, and parameterize.

The **parameterize** folder contains the core package files related to the calculation of complex parameterizations. These files can be further modified or expanded with new features.
The **examples** folder includes a file named example.py, which demonstrates the basic usage of the package.
The **tests** folder comprises unit test cases for the volume calculation method, currently covering scenarios with positive and negative radii.

# Local Installation

parent_directory > pip install .

# To run tests

src > python3 -m unittest discover tests

# To create a source distribution and built distribution files

Run the command "python3 -m build" where the pyproject.toml file is located

### Contributions are welcome! Please fork the repository and submit a pull request for review.

1. Fork the repository
2. Create a new branch: git checkout -b feature-branch-name.
3. Make your changes and commit them: git commit -m 'Add some feature'.
4. Push to the branch: git push origin feature-branch-name.
5. Submit a pull request.
