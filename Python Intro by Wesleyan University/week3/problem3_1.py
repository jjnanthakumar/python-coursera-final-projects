def problem3_1(file):
    with open(file) as f:
        c = 0
        for line in f:
            c += len(line)
            print(line.strip('\n'))
        print()
        print("There are {} letters in the file.".format(c))

# problem3_1('dummy.txt')
