import json
import random
import time

def generate_sensor_data():
    temperature = round(random.uniform(15, 35), 1)  # Temperature between 15°C and 35°C
    humidity = round(random.uniform(30, 90), 1)  # Humidity between 30% and 90%
    return {"temperature": temperature, "humidity": humidity}

def write_to_log():
    while True:
        sensor_data = generate_sensor_data()
        with open("log.json", "w") as file:
            json.dump(sensor_data, file, indent=4)
        time.sleep(2)

if __name__ == "__main__":
    write_to_log()
