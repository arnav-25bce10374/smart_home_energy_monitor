import random
import time
import datetime
import sqlite3
import os

rate_per_kwh = 8.0   
db_file = "energy.db"

devices = {
    "Fridge":    150,
    "AC":       1200,
    "TV":         80,
    "Lights":    120,
    "Computer":  300,
}


def setup_database():
    con = sqlite3.connect(db_file)
    con.execute("""
        CREATE TABLE IF NOT EXISTS readings (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            device  TEXT,
            watts   REAL,
            time    TEXT
        )
    """)
    con.commit()
    return con

def read_device(name, base_watts):
    noise = random.uniform(0.9, 1.1)
    watts = round(base_watts * noise, 1)
    now   = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"device": name, "watts": watts, "time": now}

def save_reading(con, reading):
    con.execute(
        "INSERT INTO readings (device, watts, time) VALUES (?, ?, ?)",
        (reading["device"], reading["watts"], reading["time"])
    )
    con.commit()

def total_watts(readings):
    return sum(r["watts"] for r in readings)

def estimate_cost(watts, hours=1):
    kwh  = (watts / 1000) * hours
    cost = kwh * rate_per_kwh
    return round(cost, 2)

def print_dashboard(readings):
    os.system("cls" if os.name == "nt" else "clear")   

    print("    Smart Home Energy Monitor")
    print("=" * 45)
    print(f"  Time: {datetime.datetime.now().strftime('%H:%M:%S')}")
    print("-" * 45)
    print(f"  {'Device':<15} {'Watts':>8}   {'Cost/hr':>8}")
    print("-" * 45)

    for r in readings:
        cost = estimate_cost(r["watts"])
        print(f"  {r['device']:<15} {r['watts']:>7.1f}W   ₹{cost:>6.2f}")

    print("-" * 45)
    total = total_watts(readings)
    print(f"  {'TOTAL':<15} {total:>7.1f}W   ₹{estimate_cost(total):>6.2f}/hr")
    print("=" * 45)

    if total > 2000:
        print(f"\n   High Usage! {total:.0f}W is above 2000W limit.")
    else:
        print(f"\n   Usage is normal.")

    print("\n  Press Ctrl+C to stop.\n")

def main():
    print("Starting Smart Home Energy Monitor...")
    con = setup_database()
    print(f"Database created: {db_file}")
    print("Reading devices every 3 seconds...\n")
    time.sleep(3)

    try:
        while True:
            readings = []
            for name, watts in devices.items():
                r = read_device(name, watts)
                save_reading(con, r)
                readings.append(r)

            print_dashboard(readings)

            for _ in range(3):
                time.sleep(1)

    except KeyboardInterrupt:
        print("\n\nStopped. All data saved to", db_file)
        con.close()

if __name__ == "__main__":
    main()
