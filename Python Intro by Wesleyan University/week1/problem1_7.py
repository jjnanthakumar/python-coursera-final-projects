def problem1_7():
    b1 = int(input("Enter the length of one of the bases: "))
    b2 = int(input("Enter the length of the other base: "))
    h = int(input("Enter the height: "))
    print("The area of a trapezoid with bases {} and {} and height {} is {}".format(float(b1), float(b2), float(h),0.5 * (b1 + b2) * h))
