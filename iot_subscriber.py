import paho.mqtt.client as mqtt
import json
from gpiozero import LED, OutputDevice

# GPIO αντιστοιχίσεις
led_pins = {
    "blue": LED(18),
    "green": LED(23),
    "yellow": LED(24),
    "red": LED(25)
}

buzzer = OutputDevice(27)
heating_relay = OutputDevice(22)

def clear_leds():
    for led in led_pins.values():
        led.off()

# MQTT callbacks
def on_connect(client, userdata, flags, rc):
    print("Συνδέθηκε στο MQTT broker")
    client.subscribe("led_control")
    client.subscribe("buzzer_control")
    client.subscribe("heating_control")

def on_message(client, userdata, msg):
    topic = msg.topic
    try:
        payload = json.loads(msg.payload.decode())
        print(f"[{topic}] Received: {payload}")

        # ---- LED Control ----
        if topic == "led_control":
            clear_leds()
            led_color = payload.get("led")
            if led_color in led_pins:
                led_pins[led_color].on()
                print(f"LED ON: {led_color}")

        # ---- Buzzer Control ----
        elif topic == "buzzer_control":
            if payload.get("buzzer") is True:
                buzzer.on()
                print("Buzzer ON")
            else:
                buzzer.off()
                print("Buzzer OFF")

        # ---- Heating / Relay Control ----
        elif topic == "heating_control":
            if payload.get("heating") is True:
                heating_relay.on()
                print("Θέρμανση ON (Ρελέ Ενεργό)")
            else:
                heating_relay.off()
                print("Θέρμανση OFF (Ρελέ Ανενεργό)")

    except Exception as e:
        print("Σφάλμα:", e)

# MQTT Setup
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.1.51", 1883, 60)  

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Έξοδος...")
finally:
    clear_leds()
    buzzer.off()
    heating_relay.off()
