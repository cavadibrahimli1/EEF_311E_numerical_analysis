![image](https://github.com/cavadibrahimli1/EEF_311E_numerical_analysis/assets/76445357/d288a2c0-b91b-4584-9880-a3614f3373d7)


# Numerical Analysis with Python - Polynomial Root Finder

This repository contains a Python program for finding the roots of polynomials using the bisection method. The program reads coefficients of polynomials from the input.txt file, calculates the roots, and writes the results to the output.txt file.

## Course Information
- Course: EEF 311E Numerical Analysis with Python
- Instructor: Academic Dr. Bora Döken
- Student: Javad Ibrahimli
- Student ID: 040210932
- Date: 11/12/2023
- Assignment: HW2
- Code Editor: Visual Studio Code 1.61.2
- Python Version: 3.9
- Operating System: Windows 11



## Functions

- polynomial_adjuster(coefficients, x)
Evaluates a polynomial with given coefficients at a given x value using Horner's method.

- bisection_rootfinder(coefficients, a, b, c=1e-6, max_iterations=100)
Finds the root of a polynomial using the bisection method within a specified interval.

- equation_structure(coefficients)
Formats the polynomial equation in a readable form.

- root_structure(root)
Formats the root in a readable form.

- file_scanner(filename)
Scans the file and returns the coefficients of the polynomials.

## Usage

1. Ensure Python 3.9 is installed on your system.
2. Clone the repository

```bash
  git clone https://github.com/yourusername/yourrepository.git
```
3. Navigate to the project directory:
4. Run the main script

python 6583314.py

```bash
    python 6583314.py    
```

## License
This project is licensed under the MIT License 
