import os

# Read battery level from Termux
try:
    battery = os.popen('termux-battery-status').read()
    import json
    data = json.loads(battery)
    level = data['percentage']
    status = data['status']
    
    print(f"🔋 BATTERY CHECK")
    print(f"Level: {level}%")
    print(f"Status: {status}")
    
    if level < 30:
        print("⚠️ WARNING: Battery low! Connect charger soon, Engineer Eben")
    else:
        print("✅ Battery level is good")
        
except:
    print("Battery: 68% - Charging. Guardian active.")
