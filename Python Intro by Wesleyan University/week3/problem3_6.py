import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1, 'r') as f:
    for leng in [str(len(line.strip('\n'))) for line in f.readlines()]:
        with open(file2, 'a') as f1:
            f1.writelines(leng + '\n')
