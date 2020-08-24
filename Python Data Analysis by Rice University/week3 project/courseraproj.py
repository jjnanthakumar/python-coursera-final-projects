__author__="jjnanthakumar477@gmail.com"
"""
Project for Week 3 of "Python Data Analysis".
Read and write CSV files using a dictionary of dictionaries.
Be sure to read the project description page for further information
about the expected behavior of the program.
"""
import csv


def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      A list of strings corresponding to the field names in
      the given CSV file.
    """
    with open(filename, 'rt') as csv_file:
        read = csv.reader(csv_file, delimiter=separator, quotechar=quote)
        return next(read)


def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """

    with open(filename, 'r') as csv_file:
        csv_file = csv.DictReader(csv_file, delimiter=separator, quotechar=quote)

    return list(csv_file)


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    with open(filename, 'r') as csv_file:
        table = {}
        csv_file = csv.DictReader(csv_file, delimiter=separator, quotechar=quote)
        for row in csv_file:
            table[row[keyfield]] = row
    return table


def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """
    table1 = []
    for dit in table:
        table2 = []
        for fieldname in fieldnames:
            table2.append(dit[fieldname])
        table1.append(table2)
    fname = open(filename, 'w', newline='')
    csv_w = csv.writer(fname, delimiter=separator, quotechar=quote, quoting=csv.QUOTE_NONNUMERIC)
    csv_w.writerow(fieldnames)
    for dt2 in table1:
        csv_w.writerow(dt2)
    fname.close()
