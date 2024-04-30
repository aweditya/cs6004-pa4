import random
import sys

# Function to generate a random arithmetic operation
def generate_operation():
    operations = ['+', '-', '*']
    return random.choice(operations)

# Function to generate a random expression using variables up to ai-1
def generate_expression(i):
    expression = "a0"
    for j in range(1, i):
        operation = generate_operation()
        variable = f"a{j}"
        expression += f" {operation} {variable}"
    return expression

# Function to generate a single method
def generate_method(method_number, num_variables, num_constants):
    method_code = f"\tpublic static void method{method_number}() {{\n"
    
    # Assign random constant values to a0 to a<num_constants - 1>
    for i in range(num_constants):
        constant_value = i+1
        method_code += f"\t\tdouble a{i} = {constant_value};\n"
    
    # Generate expressions for a<num_constants> to a<num_variables - 1>
    for i in range(num_constants, num_variables):
        expression = generate_expression(i)
        method_code += f"\t\tdouble a{i} = {expression};\n"
    
    # Print the sum of all variables
    sum_expression = "a0"
    for i in range(1, num_variables):
        sum_expression += f" + a{i}"
    method_code += f"\t\tSystem.out.println({sum_expression});\n"
    
    method_code += "\t}\n"
    return method_code

# Function to generate the Java program with specified parameters
def generate_java_program(num_methods, num_variables, num_constants, num_iters):
    java_program = "import java.util.*;\npublic class Test {\n"
    
    # Generate methods
    for i in range(1, num_methods + 1):
        java_program += generate_method(i, num_variables, num_constants)
    
    # Main method calling all methods in a loop for a billion iterations
    java_program += "\tpublic static void main(String[] args) {\n"
    java_program += f"\t\t for (int i = 0; i < {num_iters}; i++)"
    java_program += "{\n"
    for i in range(1, num_methods + 1):
        java_program += f"\t\t\tmethod{i}();\n"
    java_program += "\t\t}\n\t}\n}"

    return java_program

if __name__ == "__main__":
    # Check if filename is provided as argument
    if len(sys.argv) != 2:
        print("Usage: python test-gen.py <output_file>")
        sys.exit(1)

    output_file = sys.argv[1]

    # Parameters    
    num_methods = 100
    num_variables = 50
    num_constants = 10
    num_iters = 500000

    # num_methods = 10
    # num_variables = 10
    # num_constants = 3
    # num_iters = 10000

    # Generate the Java program with specified parameters
    java_code = generate_java_program(num_methods, num_variables, num_constants, num_iters)

    # Write the Java program to the output file
    with open(output_file, "w") as file:
        file.write(java_code)

    print(f"Java program written to {output_file}.")

