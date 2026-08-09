import os
import subprocess
from datetime import datetime

# ===== OMNI-OPERATOR v10.0 =====
# Engineer: Eben | The Machine That SEES
# Mission: Scan Real Data + Detect Problem + Provide Solution
# For: Phones, Servers, Industries
# =================================

def log_activity(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("guardian_log.txt", "a") as f:
        f.write(f"[{now}] {message}\n")

def get_battery_temp():
    try:
        # Works on most Android phones via Termux
        result = subprocess.check_output("dumpsys battery | grep temperature", shell=True).decode()
        temp = int(result.split(":")[1].strip()) / 10
        return temp
    except:
        return "N/A"

def show_dashboard(status, problems, actions):
    os.system('clear')
    print("="*55)
    print(" 🤖 OMNI-OPERATOR v10.0 - LIVE PROBLEM DETECTING")
    print(" Engineer Eben | For Industries & Organizations")
    print("="*55)
    print(f" System Status: {status}")
    print(f" Problems Detected:")
    for p in problems:
        print(f" - {p}")
    print(f" Actions Taken:")
    for a in actions:
        print(f" - {a}")
    print(f" Time: {datetime.now().strftime('%I:%M:%S %p')}")
    print("="*55)

def ai_autopilot():
    problems = []
    actions = []
    
    print(">>> SCANNING LIVE SYSTEM...")
    
    # LIVE DETECTION 1: BATTERY TEMP
    temp = get_battery_temp()
    if temp!= "N/A" and temp > 38:
        problems.append(f"Battery Temperature: {temp}C - CRITICAL HOT")
        status = "CRITICAL"
    else:
        status = "OPTIMAL"
    
    # SOLUTION ENGINE
    if status == "CRITICAL":
        print(">>> PROBLEM FOUND: Phone Overheating")
        actions.append("Closed Recent Apps - Battery Cooling")
        os.system('am broadcast -a com.android.systemui.recent')
        
        actions.append("Opened Settings for Manual Cooling")
        os.system('am start -a android.settings.SETTINGS')
    
    show_dashboard(status, problems, actions)
    log_activity(f"v10.0 SCAN: Status={status}, Problems={len(problems)}")
    print("\n🔥 AI BRAIN: MISSION COMPLETE.")
    print("Scan Complete. Machine Stopped.")

log_activity("OMNI v10.0 STARTED")
ai_autopilot()
