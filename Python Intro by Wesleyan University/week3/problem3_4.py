import calendar


def problem3_4(mon, day, year):
    c = 0
    for i in calendar.month_name:
        if i == mon:
            print("{}/{}/{}".format(c, day, year))
        c += 1

# problem3_4("July", 17, 2016)
