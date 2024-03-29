def add_time(start, duration, day_of_week=False):
    days_of_the_week_index = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5,
                              "sunday": 6}
    days_of_the_week_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # duration
    duration_tuple = duration.partition(":")
    duration_hour = int(duration_tuple[0])
    duration_minute = int(duration_tuple[2])

    # start time
    start_tuple = start.partition(":")
    start_tuple_minute = start_tuple[2].partition(" ")
    start_hour = int(start_tuple[0])
    start_minute = int(start_tuple_minute[0])

    # Am_Pm working
    am_or_pm = start_tuple_minute[2]
    am_or_pm_flip = {"AM": "PM", "PM": "AM"}

    # days_of_the_week
    amount_of_days = int(duration_hour / 24)

    if (am_or_pm == "PM"):
        start_hour += 12
    # End time
    end_hour = (start_hour + duration_hour)
    end_minute = start_minute + duration_minute
    if (end_minute >= 60):
        end_hour += 1
        end_minute = end_minute % 60

    print(end_hour, "111")

    amount_of_am_pm_flips = int((end_hour % 24)

    end_minute = end_minute if end_minute > 9 else "0" + str(end_minute)

    if amount_of_am_pm_flips > 12:
        am_or_pm = "pppPM"
    elif amount_of_am_pm_flips < 12:
        am_or_pm = "pppAM"
    else:
        am_or_pm = "Bruv, wtf"

    print(end_hour)
    # end_hour = end_hour%12
    end_hour = 12 if end_hour == 0 else end_hour

    print(end_hour)

    # days_of_the_week (2)
    if (am_or_pm == "PM" and (start_hour + duration_hour % 12) >= 12):
        amount_of_days += 1

    returnTime = str(end_hour) + ":" + str(end_minute) + " " + am_or_pm

    if (day_of_week):
        day_of_week = day_of_week.lower()
    index = int(days_of_the_week_index[day_of_week] + amount_of_days) % 7
    new_day = days_of_the_week_array[index]
    returnTime += ", " + new_day

    if (amount_of_days == 1):
        return returnTime + " " + ("(next day)")
    elif (amount_of_days > 1):
    return returnTime + " (" + str(amount_of_days) + " days later)"


return returnTime
