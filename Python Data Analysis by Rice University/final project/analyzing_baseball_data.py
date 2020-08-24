"""
Project for Week 4 of "Python Data Analysis".
Processing CSV files with baseball stastics.
Be sure to read the project description page for further information
about the expected behavior of the program.
"""
import csv

__author__ = "jjnanthakumar477@gmail.com"


# codes from week3 project
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
    table = []
    with open(filename, 'r') as csv_file:
        csv_file = csv.DictReader(csv_file, delimiter=separator, quotechar=quote)
        for ele in csv_file:
            table.append(ele)
        print(table)
    return table


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


MINIMUM_AB = 500


def batting_average(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the batting average as a float
    """
    hits = float(batting_stats[info["hits"]])
    at_bats = float(batting_stats[info["atbats"]])
    if at_bats >= MINIMUM_AB:
        return hits / at_bats
    else:
        return 0


def onbase_percentage(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the on-base percentage as a float
    """
    hits = float(batting_stats[info["hits"]])
    at_bats = float(batting_stats[info["atbats"]])
    walks = float(batting_stats[info["walks"]])
    if at_bats >= MINIMUM_AB:
        return (hits + walks) / (at_bats + walks)
    else:
        return 0


def slugging_percentage(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the slugging percentage as a float
    """
    hits = float(batting_stats[info["hits"]])
    doubles = float(batting_stats[info["doubles"]])
    triples = float(batting_stats[info["triples"]])
    home_runs = float(batting_stats[info["homeruns"]])
    singles = hits - doubles - triples - home_runs
    at_bats = float(batting_stats[info["atbats"]])
    if at_bats >= MINIMUM_AB:
        return (singles + 2 * doubles + 3 * triples + 4 * home_runs) / at_bats
    else:
        return 0


def filter_by_year(statistics, year, yearid):
    """
    Inputs:
      statistics - List of batting statistics dictionaries
      year       - Year to filter by
      yearid     - Year ID field in statistics
    Outputs:
      Returns a list of batting statistics dictionaries that
      are from the input year.
    """
    return [dit for dit in statistics if dit[yearid] == str(year)]


def top_player_ids(info, statistics, formula, numplayers):
    """
    Inputs:
      info       - Baseball data information dictionary
      statistics - List of batting statistics dictionaries
      formula    - function that takes an info dictionary and a
                   batting statistics dictionary as input and
                   computes a compound statistic
      numplayers - Number of top players to return
    Outputs:
      Returns a list of tuples, player ID and compound statistic
      computed by formula, of the top numplayers players sorted in
      decreasing order of the computed statistic.
    """
    table = [(dic[info['playerid']], formula(info, dic)) for dic in statistics]
    table = sorted(table, key=lambda x: x[1], reverse=True)
    return table[0:numplayers]


def lookup_player_names(info, top_ids_and_stats):
    """
    Inputs:
      info              - Baseball data information dictionary
      top_ids_and_stats - list of tuples containing player IDs and
                          computed statistics
    Outputs:
      List of strings of the form "x.xxx --- FirstName LastName",
      where "x.xxx" is a string conversion of the float stat in
      the input and "FirstName LastName" is the name of the player
      corresponding to the player ID in the input.
    """
    m_stat = read_csv_as_list_dict(info['masterfile'], info['separator'], info['quote'])
    table = []
    for ids in top_ids_and_stats:
        for dit in m_stat:
            if dit[info['playerid']] == ids[0]:
                table.append('{0:.3f} --- {1} {2}'.format(ids[1], dit[info['firstname']], dit[info['lastname']]))
    return table


def compute_top_stats_year(info, formula, numplayers, year):
    """
    Inputs:
      info        - Baseball data information dictionary
      formula     - function that takes an info dictionary and a
                    batting statistics dictionary as input and
                    computes a compound statistic
      numplayers  - Number of top players to return
      year        - Year to compute top statistics for
    Outputs:
      Returns a list of strings for the top numplayers in the given year
      according to the given formula.
    """
    b_stat = read_csv_as_list_dict(info['battingfile'], info['separator'], info['quote'])
    s_year = filter_by_year(b_stat, year, info['yearid'])
    top = top_player_ids(info, s_year, formula, numplayers)
    result_list = lookup_player_names(info, top)
    return result_list


def aggregate_by_player_id(statistics, playerid, fields):
    """
    Inputs:
      statistics - List of batting statistics dictionaries
      playerid   - Player ID field name
      fields     - List of fields to aggregate
    Output:
      Returns a nested dictionary whose keys are player IDs and whose values
      are dictionaries of aggregated stats.  Only the fields from the fields
      input will be aggregated in the aggregated stats dictionaries.
    """
    dictt = {}

    for dit in statistics:
        dictt[dit[playerid]] = {}
        for field in fields:
            dictt[dit[playerid]][field] = 0
            dictt[dit[playerid]][playerid] = dit[playerid]

    # Everything is set up, only addition of fields is pending
    # print(d)
    for key in dictt:
        for dit in statistics:
            if key == dit[playerid]:
                # print(True)
                for stat in fields:
                    dictt[key][stat] += int(dit[stat])
    return dictt


def compute_top_stats_career(info, formula, numplayers):
    """
    Inputs:
      info        - Baseball data information dictionary
      formula     - function that takes an info dictionary and a
                    batting statistics dictionary as input and
                    computes a compound statistic
      numplayers  - Number of top player
      s to return
    """
    bat_stat = read_csv_as_list_dict(info['battingfile'], info['separator'], info['quote'])

    fieldnames = info['battingfields']

    # numplayers = 4

    indiv_player_stat = aggregate_by_player_id(bat_stat, info['playerid'], fieldnames)

    # print(indiv_player_stat)

    # separate player names from aggregate by player ID:

    player_name = [key for key, val in indiv_player_stat.items()]

    # print(player_name)

    # compunded stats for each player:

    compounded_stat = []

    for player in player_name:
        compounded_stat.append((player, formula(info, indiv_player_stat[player])))

    # Sort the compounded stat:

    # print(compounded_stat)

    # now look up player names:

    compounded_stat = sorted(compounded_stat, key=lambda x: x[1], reverse=True)

    return lookup_player_names(info, compounded_stat[0:numplayers])
