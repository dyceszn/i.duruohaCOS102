usersInput = int(input('Enter your choice:\nSelect 1 for Quadratic Equation\nSelect 2 for Cubic Equation\nSelect 3 for Quartic Equation\n'))

if usersInput == 1:     # Quardratic
    A = float(input('Enter value for A:'))
    B = float(input('Enter value for B:'))
    C = float(input('Enter value for C:'))
    # solving quadratic equation via quadratic formular:
    discriminant = (B**2 - 4 * A * C)**0.5
    x1 = (-B + discriminant) /(2 * A)
    x2 = (-B - discriminant) /(2 * A)
    print(f'The roots of the equations are:{x1} and {x2}')

elif usersInput == 2:   # Cubic equation
    A = float(input('Enter value for A:'))
    B = float(input('Enter value for B:'))
    C = float(input('Enter value for C:'))
    D = float(input('Enter value for D:'))
    # solving cubic equation by trial and error from a range of integers only:
    roots = []
    for i in range(-100, 101):
        x = i
        equation = (A * x ** 3) + (B * x ** 2) + (C * x) + D
        if equation == 0.0:
            roots.append(x)
    if len(roots) == 0:
        print('No roots found')
    else:
        print(f'The roots are: {roots}')

elif usersInput == 3:   # Quartic equation
    A = float(input('Enter value for A:'))
    B = float(input('Enter value for B:'))
    C = float(input('Enter value for C:'))
    D = float(input('Enter value for D:'))
    E = float(input('Enter value for E:'))
    # solving quartic equation by trial and error from a range of integers only:
    roots = []
    for i in range(-100, 101):
        x = i
        equation = (A * x ** 4) + (B * x ** 3) + (C * x ** 2) + (D * x) + E
        if equation == 0.0:
            roots.append(x)
    if len(roots) == 0:
        print('No roots found')
    else:
        print(f'The roots are: {roots}')
else:
    print('Invalid Input')




