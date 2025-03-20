import psutil
from pynotifier import Notification

battery = psutil.sensors_battery()

if battery is None:
    print("No battery information available.")
else:
    plugged = battery.power_plugged
    percent = battery.percent
    if percent <= 20 and not plugged:
        Notification(
            title="Battery Low",
            description=f"{percent}% Battery remaining!",
            duration=5
        ).send()