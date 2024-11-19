# IoT Shield - Real-Time Anomaly Detection for Cybersecurity in IoT Devices

## Overview

The **IoT Shield** project was developed during the **MIS Breakthrough Hackathon**, organized by SFU MISA (Management Information Systems Association) and hosted at the Microsoft Vancouver office. Our team tackled critical cybersecurity challenges associated with IoT devices in enterprise environments by designing a predictive anomaly detection system.

The solution leverages machine learning to:
1. **Simulate Real-Time IoT Data**: Generate realistic telemetry from devices like cameras, thermostats, and sensors.
2. **Detect Anomalies**: Use Isolation Forest to identify unusual device behavior based on temperature, activity, and battery metrics.
3. **Provide Dynamic Visualization**: Deliver clear, color-coded visualizations for actionable insights on compromised devices.

We also integrated **Copilot**, an AI-powered tool, to enhance the speed and efficiency of development while innovating within a tight time frame.

---

## Hackathon Context

This project was developed in **under 48 hours** as part of the **MIS Breakthrough Hackathon**, a high-pressure event encouraging innovation in solving real-world cybersecurity issues. The event focused on integrating **AI tools like Copilot** to accelerate development and foster collaborative problem-solving.

Our key objectives:
- Build a scalable solution for securing IoT devices in workplaces.
- Analyze historical and real-time data to proactively detect unusual device behavior.
- Enable enterprise environments to mitigate IoT security risks in real-time.

Hosted at **Microsoft Vancouver**, the hackathon provided valuable mentorship and insights from industry professionals, including **John Westworth (Director of the Garage)**.

---

## Features

- **IoT Data Simulation**: Generates realistic telemetry data for 400 devices, including temperature, activity level, and battery metrics.
- **Device-Specific Risk Models**: Implements customizable risk thresholds for each device type (e.g., Cameras: 8% anomaly rate).
- **Real-Time Anomaly Detection**: Uses Isolation Forest to detect and flag unusual device behavior dynamically.
- **Dynamic Visualization**: Animates anomalies in real time, with color-coded markers indicating device type and anomaly status.

---

## Setup and Execution

### Prerequisites
- Python 3.10+
- Required Libraries: `numpy`, `pandas`, `matplotlib`, `scikit-learn`

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/username/IoT-Shield-Hackathon.git
