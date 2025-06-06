import adafruit_dht
import board
import time
import json
import paho.mqtt.client as mqtt
from gpiozero import InputDevice

# Αισθητήρας θερμοκρασίας/υγρασίας (DHT22 στο GPIO4)
dht_sensor = adafruit_dht.DHT22(board.D4)

# Αισθητήρας καπνού (MQ5 στο GPIO17)
smoke_sensor = InputDevice(17)

# MQTT ρυθμίσεις
MQTT_BROKER = "192.168.1.51"
MQTT_PORT = 1883
MQTT_TOPIC = "fire_status"
DEVICE_ID = "sensor_pi_5"

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

try:
    while True:
        try:
            temperature = dht_sensor.temperature
            humidity = dht_sensor.humidity
            smoke_detected = smoke_sensor.is_active  # True/False

            if temperature is not None and humidity is not None:
                payload = {
                    "device_id": DEVICE_ID,
                    "temperature": round(temperature, 2),
                    "humidity": round(humidity, 2),
                    "smoke": bool(smoke_detected),
                    "unit": "C"
                }

                client.publish(MQTT_TOPIC, json.dumps(payload))
                print("MQTT Sent:", payload)
            else:
                print("DHT Sensor read error")

        except Exception as e:
            print("Sensor error:", e)

        time.sleep(5)

except KeyboardInterrupt:
    print("Stopped by user")
