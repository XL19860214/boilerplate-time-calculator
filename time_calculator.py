def add_time(start, duration, day=None):
    startSplit = start.split()
    timeSplit = startSplit[0].split(':')
    hours = int(timeSplit[0])
    minutes = int(timeSplit[1])
    side = startSplit[1]

    newHours = hours
    if side == 'PM':
        newHours += 12

    durationSplit = duration.split(':')
    dHours = int(durationSplit[0])
    dMinutes = int(durationSplit[1])

    days = dHours // 24
    spare = dHours % 24

    newMinutes = minutes + dMinutes
    if newMinutes >= 60:
        newHours += 1
        newMinutes -= 60

    newHours += spare
    if newHours >= 24:
        days += 1
        newHours -= 24
    
    newSide = 'AM'
    if newHours > 12:
        newSide = 'PM'
        newHours -= 12
    if newHours == 12 and newMinutes > 0:
        newSide = 'PM'

    # Fix for Requirement
    if newSide == 'AM' and newHours == 0:
        newHours = 12
    
    newTime = '{:d}:{:02d} {:s}'.format(newHours, newMinutes, newSide)

    if day:
        newTime += ', ' + getDay(day.lower(), days).capitalize()

    if days > 0:
        if days == 1:
            newTime += ' (next day)'
        else:
            newTime += ' ({:d} days later)'.format(days)


    return newTime


def getDay(weekday, duration):
    weekdays = [
        'sunday',
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday'
    ]

    return weekdays[(weekdays.index(weekday) + duration % 7) % 7]
