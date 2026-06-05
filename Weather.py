def estimate_arrival(distance_km, weather_condition):
    total_time = distance_km * 3

    if weather_condition == "rainy":
        total_time += 10

    return total_time

print(estimate_arrival(10, "sunny"))
print(estimate_arrival(10, "rainy"))
