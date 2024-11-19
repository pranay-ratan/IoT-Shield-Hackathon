import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
import random
import matplotlib.animation as animation

# Step 1: Simulate IoT Telemetry Data with Device Types and Multiple Criteria
def simulate_iot_data(n=400):
    np.random.seed(0)
    device_types = ['Camera', 'Thermostat', 'Sensor', 'Door Lock', 'Light Bulb']
    data = {
        'device_id': [f'device_{i}' for i in range(n)],
        'device_type': [random.choice(device_types) for _ in range(n)],
        'temperature': np.random.normal(25, 3, n).tolist(),  # Normal temperature around 25°C
        'activity': np.random.normal(50, 5, n).tolist(),      # Normal activity level around 50
        'battery_level': np.random.normal(80, 10, n).tolist() # Normal battery level around 80%
    }

    # Introduce anomalies in various criteria based on risk levels
    risk_levels = {
        'Camera': 0.08,      # 8% anomaly rate for cameras
        'Thermostat': 0.04,  # 4% anomaly rate for thermostats
        'Sensor': 0.05,      # 5% anomaly rate for sensors
        'Door Lock': 0.10,   # 10% anomaly rate for door locks
        'Light Bulb': 0.03   # 3% anomaly rate for light bulbs
    }

    for device_type, anomaly_rate in risk_levels.items():
        type_indices = [i for i, x in enumerate(data['device_type']) if x == device_type]
        num_anomalies = int(len(type_indices) * anomaly_rate)
        for _ in range(num_anomalies):
            idx = random.choice(type_indices)
            data['temperature'][idx] = np.random.uniform(70, 100)   # Abnormal high temperature
            data['activity'][idx] = np.random.uniform(0, 10)        # Abnormal low activity
            data['battery_level'][idx] = np.random.uniform(5, 20)   # Abnormal low battery level

    return pd.DataFrame(data)

# Step 2: Detect Anomalies with Isolation Forest using Device-specific Contamination Levels
def detect_anomalies(data):
    risk_levels = {
        'Camera': 0.08,
        'Thermostat': 0.04,
        'Sensor': 0.05,
        'Door Lock': 0.10,
        'Light Bulb': 0.03
    }

    anomaly_data = pd.DataFrame()
    for device_type, contamination in risk_levels.items():
        subset = data[data['device_type'] == device_type].copy()
        model = IsolationForest(contamination=contamination)
        subset['anomaly'] = model.fit_predict(subset[['temperature', 'activity', 'battery_level']])
        subset['anomaly'] = subset['anomaly'].apply(lambda x: 'Normal' if x == 1 else 'Anomaly')
        anomaly_data = pd.concat([anomaly_data, subset])

    return anomaly_data

# Step 3: Dynamic Plotting of IoT Devices with Animation
def animate(i, data, ax, device_types, colors):
    ax.clear()
    device_type = device_types[i % len(device_types)]
    subset = data[data['device_type'] == device_type]

    # Plot each device type with different color and highlight anomalies
    for anomaly_status, color in colors[device_type].items():
        filtered_data = subset[subset['anomaly'] == anomaly_status]
        ax.scatter(filtered_data['temperature'], filtered_data['activity'],
                   color=color, label=f"{device_type} - {anomaly_status}", s=100, alpha=0.6, edgecolors='k')

    ax.set_xlabel('Temperature')
    ax.set_ylabel('Activity Level')
    ax.set_title(f"IoT Device Anomaly Detection for {device_type}")
    ax.legend(loc='upper left')
    ax.grid(True)

# Main Execution
iot_data = simulate_iot_data(400)
anomaly_data = detect_anomalies(iot_data)

# Define colors for each device type and anomaly status
device_types = ['Camera', 'Thermostat', 'Sensor', 'Door Lock', 'Light Bulb']
colors = {
    'Camera': {'Normal': 'blue', 'Anomaly': 'red'},
    'Thermostat': {'Normal': 'green', 'Anomaly': 'orange'},
    'Sensor': {'Normal': 'purple', 'Anomaly': 'brown'},
    'Door Lock': {'Normal': 'cyan', 'Anomaly': 'magenta'},
    'Light Bulb': {'Normal': 'yellow', 'Anomaly': 'black'}
}

# Initialize figure and axis for dynamic plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Animate by updating the plot every second for a new device type
ani = animation.FuncAnimation(fig, animate, frames=len(device_types), fargs=(anomaly_data, ax, device_types, colors),
                              interval=1000, repeat=True)

plt.show()

# Output IoT devices that are flagged as anomalies
anomalous_devices = anomaly_data[anomaly_data['anomaly'] == 'Anomaly']
print("Flagged IoT Devices:")
print(anomalous_devices[['device_id', 'device_type', 'temperature', 'activity', 'battery_level']])