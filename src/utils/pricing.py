def calculate_premium(age, vehicle_age, damaged):
    base = 5000
    if age < 25: base *= 1.5
    if vehicle_age > 10: base *= 1.2
    if damaged: base += 2000
    return base