# IoT Fire & Smart Thermostat Project (Raspberry Pi + MQTT + Node-RED)

## Περιγραφή

Η εργασία αυτή αποτελεί μια ολοκληρωμένη IoT εφαρμογή με στόχο την:

- **Ανίχνευση θερμοκρασίας, υγρασίας και καπνού**
- **Οπτική αναπαράσταση δεδομένων σε Dashboard (Node-RED)**
- **Έλεγχο LEDs, buzzer και ρελέ μέσω MQTT**
- **Προσομοίωση έξυπνου θερμοστάτη (Smart Thermostat)**

## Υλικό (Hardware)

- Raspberry Pi 5
- Αισθητήρας DHT22 (θερμοκρασία/υγρασία)
- Αισθητήρας καπνού MQ-5 (ψηφιακή έξοδος)
- 4 LEDs (μπλε, πράσινο, κίτρινο, κόκκινο)
- Buzzer (active)
- Ρελέ 1 καναλιού
- Breadboard & jumper wires

## Δομή Project

iot-fire-project/
├── fire_publisher.py       # Δημοσίευση δεδομένων αισθητήρων
├── iot_subscriber.py       # Έλεγχος LEDs, buzzer, ρελέ μέσω MQTT
├── requirements.txt        # Python βιβλιοθήκες
└── README.md               # Οδηγίες χρήσης (αυτό το αρχείο)

1. Εγκατάσταση (Python περιβάλλον)
Δημιούργησε virtual environment:
python3 -m venv venv
source venv/bin/activate

2. Εγκατάσταση εξαρτήσεων:
pip install -r requirements.txt

3. Εκτέλεση
Άνοιξε 2 τερματικά:

Terminal 1 – Αποστολή δεδομένων:
python3 fire_publisher.py

Terminal 2 – Λήψη εντολών / Έλεγχος εξόδων:
python3 iot_subscriber.py

## Λειτουργίες

LEDs: Ανάβουν ανάλογα με τη θερμοκρασία (4 ζώνες)

Buzzer: Ενεργοποιείται όταν ανιχνεύεται καπνός

Ρελέ: Αντιπροσωπεύει θέρμανση (ON/OFF)

Node-RED Dashboard:

Δέχεται επιθυμητή θερμοκρασία

Συγκρίνει με πραγματική θερμοκρασία

Ενεργοποιεί το ρελέ μέσω MQTT

Δείχνει ενδείξεις με emoji, γραφήματα και LED icons

Dashboard URL: http://192.168.Χ.Χ:1880/ui

Δημιουργός: Βασίλειος Μητσοκάπας
Καθηγητής: Παναγιώτης Καρκαζής
Πανεπιστήμιο Δυτικής Αττικής – ΠΜΣ Προηγμένες Τεχνολογίες Υπολογιστικών Συστημάτων
Έτος: 2025
