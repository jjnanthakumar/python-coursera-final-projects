__author__ = "jjnanthakumar477@gmail.com"
""" This is Coursera final Project using Files """

IDENTICAL = -1


def singleline_diff(line1, line2):
    """
        Inputs:
          line1 - first single line string
          line2 - second single line string
        Output:
          Returns the index where the first difference between
          line1 and line2 occurs.

          Returns IDENTICAL if the two lines are the same.
        """
    end = min(len(line1), len(line2))
    for i_1 in range(end):
        if line1[i_1] != line2[i_1]:
            return i_1
    if len(line1) != len(line2):
        return end
    return -1


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    new_str = ""
    end = max(len(line1), len(line2))
    if idx == -1 or (idx > len(line1) or idx > len(line2)):
        return ""
    elif len(line1) == 0 and len(line2) == 0:
        new_str += '^'
    for i_1 in range(end):
        if i_1 != idx:
            new_str += '='
        else:
            new_str += '^'
            break
    return '''{}
{}
{}
'''.format(line1, new_str, line2)


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    if lines1 == lines2:
        return (IDENTICAL, IDENTICAL)
    line_no = singleline_diff(lines1, lines2)
    len_lines1, len_lines2 = len(lines1), len(lines2)

    if len_lines1 == len_lines2:
        idx = singleline_diff(lines1[line_no], lines2[line_no])
        return (line_no, idx)
    else:
        return (line_no, 0)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    new_lines = []
    with open(filename, 'r') as f_hand:
        for line in f_hand:
            new_lines.append(line.strip())
        return new_lines


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)
    tuple1 = multiline_diff(lines1, lines2)
    if tuple1 == (IDENTICAL, IDENTICAL):
        return "No differences\n"
    else:
        line_index = tuple1[0]
        string_index = tuple1[1]
        if (lines1 != [] and lines2 != []):
            line1 = lines1[line_index]
            line2 = lines2[line_index]
            diff_1 = singleline_diff_format(line1, line2, string_index)
            return "Line " + str(line_index) + ":\n" + diff_1
        elif lines1 == []:
            line2 = lines2[line_index]
            return "Line 0:\n\n^\n" + line2 + "\n"
        else:
            line1 = lines1[line_index]
            return "Line 0:\n" + line1 + "\n^\n\n"
