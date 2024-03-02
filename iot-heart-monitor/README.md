# IoT Heart Attack Detection and Monitoring Device 🚑💓

## Overview
This project aims to develop an Internet of Things (IoT) based heart attack detection and heart rate monitoring device designed to operate during sleep. The device utilizes a pulse sensor, Arduino UNO, and a Wi-Fi module to collect and transmit heart rate data to an IoT platform for analysis. The system aims to detect abnormal heartbeats (arrhythmia) and alert both nearby individuals and medical emergencies in real-time.

## Key Components
- Pulse Sensor 💓
- Arduino UNO 🤖
- Wi-Fi Module (e.g., ESP8266) 📡
- Power Supply 🔌
- IoT Platform (API endpoint and API key required) 🌐
- Mobile App (Optional, for monitoring and alerts) 📱

## Software Components
- Arduino IDE for programming Arduino UNO 💻
- Python for data acquisition and transmission 🐍
- IoT Platform for data analysis and storage 📊
- Mobile App Development Tools (if creating a user interface) 🛠️

## Project Structure
- `Arduino/` - Contains the Arduino sketch for reading pulse sensor data and transmitting it to the Wi-Fi module.
- `Python/` - Holds the Python script for data acquisition and transmission to the IoT platform.
- `MobileApp/` (Optional) - If applicable, includes files related to mobile app development.

## Getting Started
1. Clone the repository: `git clone https://github.com/shashankatthaluri/project_ideashub/iot-heart-monitor.git`
2. Connect the hardware components as per the documentation.
3. Configure IoT platform details in the Python script (`Python/data_acquisition.py`).
4. Upload the Arduino sketch to the Arduino UNO.
5. Run the Python script (`Python/data_acquisition.py`) on your local machine or a Raspberry Pi.

## Testing
1. Ensure the hardware components are connected correctly.
2. Monitor the console for data transmission messages.
3. Check the IoT platform for received heart rate data.
4. Simulate abnormal heart scenarios for testing.

## Security Considerations
- Implement encryption for data transmission to protect user privacy.

## Acknowledgments
- The project idea originated from the need to address cardiac deaths during sleep.
- Inspiration drawn from existing IoT devices and solutions in the market.

## License
This project is licensed under the [MIT License](LICENSE).

## Author
Shashank atthaluri 🙌

