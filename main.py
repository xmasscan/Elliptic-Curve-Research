import addition as add

# Pretty Weierstrass Equation printing
def print_weierstrass(a):
    # All terms zeroable by respective weights
    terms = ["xy","y","x^2","x"]
    # Begin building equation
    weierstrass = "y^2" 
    # if a_1 != 0
    if a[0] != 0:
        # plus or minux sign printing (-x looks nicer than + -x)
        if a[0] < 0:
            weierstrass += " -"
        else:
            weierstrass += " +"
        # just print the term if a_1 = 1
        if abs(a[0]) == 1:
            weierstrass += " xy"
        else:
            weierstrass += f" {abs(a[0])}xy"
    # a_3 handling
    if a[1] != 0:
        if a[1] < 0:
            weierstrass += " -"
        else:
            weierstrass += " +"
        # just print the term if a_1 = 1
        if abs(a[1]) == 1:
            weierstrass += " y"
        else:
            weierstrass += f" {abs(a[1])}y"

    # left side complete, begin right side
    weierstrass += " = x^3"

    if a[2] != 0:
        if a[2] < 0:
            weierstrass += " -"
        else:
            weierstrass += " +"

        if abs(a[2]) == 1:
            weierstrass += " x^2"
        else:
            weierstrass += f" {abs(a[2])}x^2"
    if a[3] != 0: 
        if a[3] < 0:
            weierstrass += " -"
        else:
            weierstrass += " +"

        if abs(a[3]) == 1:
            weierstrass += " x"
        else:
            weierstrass += f" {abs(a[3])}x"

    if a[4] != 0:
        if a[3] < 0:
            weierstrass += " -"
        else:
            weierstrass += " +"
        weierstrass += f" {abs(a[4])}"

    print(weierstrass)

# MAIN
# a_1, a_3, a_2, a_4, a_6 in that order :)
a = ["a_1","a_3","a_2","a_4","a_6"]
weights = []
user_input_flag = False

while not user_input_flag:
    print("Input the weights for a given Weierstrass Equation of the form:")
    print("y^2 + a_1 xy + a_3y = x^3 + a_2x^2 + a_4x + a_6")
    for a_i in a:
        weights.append(int(input(f"{a_i}: ")))
    print()
    print("This will produce the equation:")
    print_weierstrass(weights) 
    print()
    response = input("Is this correct? (y/n): ")
    if response.upper() == "Y":
        user_input_flag = True
    else:
        print("Reprompting...")
        print()
        weights = []

print()

determinant = add.calculate_determinant(weights)

# If determinant is zero, terminate program with an exception.
if determinant == 0:
    print("Determinant of specified function is zero.")
    print("Aborting...")
    raise Exception("Determinant of Weierstrass Equation must be Non-Zero!")

print(f"Determinant: {determinant}")
print("Determinant non-zero, must be legal Elliptic Curve")
print()

# addition

x1 = int(input("x1:"))
y1 = int(input("y1:"))
x2 = int(input("x2:"))
y2 = int(input("y2:"))
point = add.add_points(weights,x1,y1,x2,y2)

print(f"P3 = {point[0]},{point[1]}")
