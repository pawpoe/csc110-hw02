# ------------------------------------------------------
#        Name: Paw Poe
#       Peers: N/A
#  References: Homework 2 Assignment Instructions, Lecture 8 slides
# ------------------------------------------------------


# Task 1.1:
#  Complete the function "read_two_ints" below:

def read_two_ints():
    """Asks for two integers then returns them"""
    x = int(input("give me x: "))
    y = int(input("give me y: "))
    print(x, y)
    return x, y


# Task 2.1:
#  Complete the function "compute_multadd" below:

def compute_multadd(a, b): # variables from def read_two_ints are passed on to a and b
    """This def calculates the product and sum of the input integers"""
    mult_result = (a*b)
    print("mult result:", mult_result)
    add_result = (a+b)
    print("add result:", add_result)
    return mult_result/add_result
    
# Task 3.1:
#  Complete the function "print_fancy" below:

def print_fancy(a, b, xy_multadd):
    """Prints the integers and solutions of the functions"""
    print("****************")
    print("RESULTS:")
    print("first number:", a)
    print("second number:", b)
    print("multadd result:", xy_multadd)
    print("================")
    
def main ():
    """Prints out the functions final output"""
    x, y = read_two_ints()
    xy_multadd = compute_multadd(x, y)
    print_fancy(x, y, xy_multadd)

    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
