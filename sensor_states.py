import csv
temperatures = []

with open("data/sensor_readings.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        temperatures.append(float(row["temperature"]))

if len(temperatures) == 0:
    print("No sensor readings found!")
else:
    minimum = min(temperatures)
    maximum = max(temperatures)
    average = sum(temperatures) / len(temperatures)

    print("Sensor Temperature Statistics")
    print("-----------------------------")
    print(f"Minimum temperature: {minimum} °C")
    print(f"Maximum temperature: {maximum} °C")
    print(f"Average temperature: {average:.2f} °C")