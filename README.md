# Smart Home Energy Monitor 
A simple command-line based Python project, which simulates and monitors the energy consumption of devices in a house in real-time.
## Features
- Real-time energy monitoring with a 3-second interval
- Multiple device simulation (AC, TV, Fridge, etc.)
- Calculate electricity cost per unit
- Data will be stored in a database
- Live dashboard will be available in the terminal
- High usage alert system
- Fully executable using a command line interface, no GUI required
## Technologies Used
- Python
- SQLite database
### Standard Python libraries:
- Random
- Time
- Datetime
- Sqlite3
- Os
## Installation & Setup
### 1. Clone the repository
Link for the repo - https://github.com/arnav-25bce10374/smart_home_energy_monitor.git
### 2. Run the project
Project Name - smart_home_energy_monitor
## How It Works?
- Simulate the usage of power for household appliances
- Introduces random variation to resemble actual usage
- Stores the data in an SQLite database named 'energy.db'
- Creates a live dashboard in the terminal
- Calculates the cost based on the electricity rate
## Sample Output
```
Smart Home Energy Monitor
=============================================
Time: 14:32:10
---------------------------------------------
Device          Watts     Cost/hr
---------------------------------------------
Fridge          145.2W    ₹1.16
AC             1180.5W    ₹9.44
TV               82.1W    ₹0.66
Lights          110.3W    ₹0.88
Computer        295.4W    ₹2.36
---------------------------------------------
TOTAL          1813.5W    ₹14.50/hr
=============================================

Usage is normal.
```

## Alerts
- Displays warning when total power exceeds 2000W
- Helps identify high energy usage
## Stopping the Program
- Press:
Ctrl + C to stop the program.
## Future Improvements
- IoT integration (ESP8266 / sensors)
- Web-based dashboard
- Mobile app support
- Monthly bill prediction
- Data visualization 



