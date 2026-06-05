def convert_minutes(numberofepisodes, durationperepisode):
    total_minutes = numberofepisodes * durationperepisode

    hours = total_minutes // 60
    remaining_minutes = total_minutes % 60

    return hours, remaining_minutes

hours, minutes = convert_minutes(5, 45)
print(f"{hours} jam {minutes} menit")
