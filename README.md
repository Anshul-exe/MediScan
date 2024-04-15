# MediScan Portal

In the era of digitalization, finding efficient ways to handle hefty tasks is crucial. Hence, we present MediScan, an IoT solution designed to simplify accessing and managing medical and hospital details for both patients and doctors. With MediScan, all information, including analytics, vitals, history, etc., is easily accessible through a simple RFID card scanning process.

## Features
- **ECG Scanning:** Our portal simplifies ECG scanning for patients, providing easy-to-understand results.
- **Vital Analytics with Graphs:** Detailed vital analytics are presented through intuitive graphs, aiding both patients and doctors in understanding health trends.

## Technology Stack
- **Django:** Backend framework for building the web application.
- **Python:** Primary programming language for backend logic.
- **HTML/CSS/JS:** Frontend technologies for creating the user interface.
- **Chart.js:** JavaScript library for generating interactive charts and graphs.
- **Raspberry Pi:** Used for connecting hardware components and running the server.
- **Arduino Uno/Node MCU:** Microcontrollers for interfacing with sensors and RFID components.
- **ECG Sensors:** Hardware devices for capturing ECG data.
- **RFID Sensor:** Component for scanning RFID cards to access patient information.

## Installation and Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/MediScan.git
   cd MediScan
   pip install -r requirements.txt
2. **Hardware Setup:**

  Connect ECG sensors to Arduino Uno/Node MCU.
  Connect RFID sensor to Arduino Uno/Node MCU.
  Set up Raspberry Pi for running the server.
3. Database Configuration:
  Configure database settings in settings.py.
Run the Server:
