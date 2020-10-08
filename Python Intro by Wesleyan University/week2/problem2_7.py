def problem2_7():
    s1 = int(input("Enter length of side one: "))
    s2 = int(input("Enter length of side two: "))
    s3 = int(input("Enter length of side three: "))
    s = .5 * (s1 + s2 + s3)
    print("Area of a triangle with sides {} {} {} is {}".format(float(s1), float(s2), float(s3),(s * (s - s1) * (s - s2) * (s - s3)) ** .5))
