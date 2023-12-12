##############################################################################################################
# Course: EEF 311E Numerical Analysis with Python
# Instructor: Academic Dr. Bora Döken
# Student: Javad Ibrahimli
# Student ID: 040210932
# Date: 11/12/2023
# Assignment: HW2
# Code editor: Visual Studio Code 1.61.2
# Python version: 3.9
# OS: Windows 11
# Description: This program reads the coefficients of the polynomials from the input.txt file and finds the roots of the polynomials using the bisection method. Then, it writes the roots of the polynomials to the output.txt file.
###############################################################################################################
#Functions
###############################################################################################################

# Function to evaluate a polynomial with given coefficients at a given x value (Horner's method) 
def polynomial_adjuster(coefficients, x):
    result = 0  # Initialize the result
    for i, coeff in enumerate(coefficients[::-1]):   # Iterate over the coefficients in reverse order
        if i > 0:   # Skip the constant term
            result += coeff * (x ** i)  # Multiply the coefficient with the x value raised to the power of the coefficient's index
        else:
            result += coeff  # Add the constant term to the result
    return result  # Return the result

# Function to find the root of a polynomial using the bisection method
def bisection_rootfinder(coefficients, a, b, c=1e-6, max_iterations=100): # c is the tolerance value, max_iterations is the maximum number of iterations
    fa = polynomial_adjuster(coefficients, a) # Evaluate the polynomial at the left endpoint
    fb = polynomial_adjuster(coefficients, b) # Evaluate the polynomial at the right endpoint

    if fa * fb > 0:    # Check if the endpoints have the same sign
        raise ValueError("The interval [a, b] does not bracket the root. Please change the interval.") # Raise an error if the endpoints have the same sign

    iteration_count = 1  # Start iteration count from 1. I did this because the iteration count can be at least 1 in the worst case if bisecting the interval is possible
    while (b - a) / 2 > c and iteration_count < max_iterations: # Check if the interval is greater than the tolerance value and the iteration count is less than the maximum number of iterations
        middle_point = (a + b) / 2     # Calculate the middle point of the interval
        f_middlepoint = polynomial_adjuster(coefficients, middle_point)  # Evaluate the polynomial at the middle point


        if f_middlepoint == 0:    # Check if the middle point is a root
            break
        elif f_middlepoint * fa < 0:   # Check if the middle point and the left endpoint have different signs
            b = middle_point 
        else:
            a = middle_point 

        iteration_count += 1  # Increment the iteration count

    root_value = (a + b) / 2  # Calculate the root value
    return root_value, iteration_count  # Return the root value and the iteration count

# Function to format the equation in a readable form
def equation_structure(coefficients):
    term_list = []  # Initialize the term list
    for i, coeff in enumerate(coefficients[::-1]):  # Iterate over the coefficients in reverse order
        if i == 0 and coeff == 0:  # Skip the constant term if it's 0
            continue  # Skip the constant term if it's 0
        elif i == 0:  
            term_list.append(f"{int(coeff)}")   # Add the constant term to the term list
            if coeff > 0:
                term_list.append("+")    # Add a plus sign if the constant term is positive
        elif i == 1:
            if coeff < 0:
                term_list.append(f"{'' if coeff == -1 else int(coeff)}x")  # Add the x term to the term list
            else:
                term_list.append(f"{'+' if coeff > 1 else ''}x")  # Add the x term to the term list

        else:
            term_list.append(f"{'' if coeff == -1 else int(coeff)}x**{i}")   # Add the x term to the term list

    return ''.join(term_list[::-1])   # Return the equation in a readable form

# Function to format the root in a readable form
def root_structure(root): 
    if abs(root - round(root)) < 1e-5:  # Check if the root is almost an integer (within a small epsilon)
        return str(int(round(root)))    # Convert the root to an integer if it's almost an integer (within a small epsilon)
    else:
        return f"{root:.5f}".rstrip('0').rstrip('.')  # Return the root in a readable form

# Function to scan the file and return the coefficients of the polynomials
def file_scanner(filename):  
    coefficient_values = {}  # Initialize the coefficient values dictionary
    try:
        with open(filename, "r") as file:   # Open the file in read mode
            for line_number, line in enumerate(file, start=1): # Iterate over the lines in the file
                try:
                    key, values = line.strip().split("=")   # Split the line into key and values
                    coefficients = list(map(float, values.split(',')))   # Split the values into a list of coefficients
                    coefficient_values[key] = coefficients    # Add the coefficients to the coefficient values dictionary
                except (ValueError, IndexError):    # Catch the errors
                    print(f"Error scanning line {line_number} in the file. Skipping... (Line: {line})") # Print the error message
    except FileNotFoundError:  # Catch the error
        print(f"Error: File '{filename}' not found. Exiting...")  # Print the error message
    except Exception as e:       # Catch the error
        print(f"An unexpected error occurred: {str(e)} Exiting...")    # Print the error message
    
    return coefficient_values   # Return the coefficient values dictionary


###############################################################################################################
# Main function
###############################################################################################################
def main():
    file_name = "input.txt"  # Initialize the file name. Adjust this if you want to use a different file
    equation_merger = file_scanner(file_name)  # Scan the file and return the coefficients of the polynomials

    output_line_format = [] # Initialize the output line format
    # Function to calculate the roots of the polynomials.
    def root_calculator(coefficients, first_a_value, first_b_value, interval_adjustment):
        a = first_a_value  # Initialize the left endpoint of the interval. You can change this if you want to use a different interval
        b = first_b_value  # Initialize the right endpoint of the interval. You can change this if you want to use a different interval

        while True:
            try:
                root_of_equation, iteration_count = bisection_rootfinder(coefficients, a, b) # Calculate the root of the polynomial
                break
            except ValueError: # Catch the error
                a_localizer = polynomial_adjuster(coefficients, a) # Evaluate the polynomial at the endpoints
                b_localizer = polynomial_adjuster(coefficients, b) # Evaluate the polynomial at the endpoints

                if a_localizer * b_localizer > 0:  # Check if the endpoints have the same sign. Bisection method cannot be applied if the endpoints have the same sign
                    # Both endpoints have the same sign, adjust the interval
                    a += interval_adjustment  # Adjust the left endpoint
                    b += interval_adjustment  # Adjust the right endpoint
                else:
                    if a_localizer == 0:  # Check if the left endpoint is a root
                        break
                    elif b_localizer == 0:  # Check if the right endpoint is a root
                        a = b
                        break
                    elif a_localizer * b_localizer < 0:   # Check if the endpoints have different signs
                        break
        return root_of_equation, iteration_count, a, b   # Return the root of the polynomial, the iteration count, the left endpoint of the interval, and the right endpoint of the interval

    for key, coefficients in equation_merger.items(): # Iterate over the coefficients in the equation merger dictionary
        output_line_format.append(f"The roots of {key}:") # Add the equation to the output line format
        # Calculate the roots of the polynomials
        root1, iterations1, a1, b1 = root_calculator(coefficients, -1, 1, -1) # Calculate the roots of the polynomials
        output_line_format.append(f"Interval: {a1:.1f}-{b1:.1f}") # Add the interval to the output line format
        output_line_format.append(f"Iteration={iterations1}") # Add the iteration count to the output line format
        output_line_format.append(f"x1={root_structure(root1)}")  # Add the root to the output line format
        # Calculate the roots of the polynomials
        root2, iterations2, a2, b2 = root_calculator(coefficients, 1, 2, 1) # Calculate the roots of the polynomials
        output_line_format.append(f"Interval: {a2:.1f}-{b2:.1f}")  # Add the interval to the output line format
        output_line_format.append(f"Iteration={iterations2}") # Add the iteration count to the output line format
        output_line_format.append(f"x2={root_structure(root2)}") # Add the root to the output line format
    # Write the output to the output.txt file
    with open("output.txt", "w") as output_file:
        output_file.write("Given equations:\n") # Write the given equations to the output file
        for key, equation in equation_merger.items():  # Iterate over the coefficients in the equation merger dictionary
            output_file.write(f"{key}= {equation_structure(equation)}\n") # Write the equation to the output file

        output_file.write("\n".join(output_line_format)) # Write the output line format to the output file

# Call the main function
if __name__ == "__main__":
    main()