def hours(duration):
    return duration // 3600
def minutes(duration):
    h = hours(duration)
    return (duration - (h * 3600)) // 60
def seconds(duration):
    m = minutes(duration)
    return (duration - (m * 60)) // 1