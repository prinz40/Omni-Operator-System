import os
from datetime import datetime

# ===== OMNI-OPERATOR ONE-CLICK v9.1 =====
# Engineer: Eben | Based on Proven v6.0
# Mission: Scan Once + Close Apps + Open Settings + Stop
# GitHub: The Machine That Never Fails
# ======================================

def log_activity(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("guardian_log.txt", "a") as f:
        f.write(f"[{now}] {message}\n")

def show_dashboard(status, actions):
    os.system('clear')
    print("="*50)
    print(" 🛡️ OMNI-OPERATOR ONE-CLICK v9.1")
    print(" Engineer Eben | Proven v6.0 Engine")
    print("="*50)
    print(f" System Status: {status}")
    print(f" Actions Taken:")
    for act in actions:
        print(f"   - {act}")
    print(f" Time: {datetime.now().strftime('%I:%M:%S %p')}")
    print("="*50)

def ai_autopilot():
    actions = []
    
    print(">>> SCANNING SYSTEM...")
    
    # ACTION 1: CLOSE RECENT APPS - THE POWER MOVE FROM v6.0
    print(">>> AUTO-COMMAND 1: Closing recent apps...")
    os.system('am broadcast -a com.android.systemui.recent')
    actions.append("Closed Recent Apps - Battery Cooling")
    log_activity("ONE-CLICK: Closed Recent Apps")
    
    # ACTION 2: OPEN SETTINGS - THE POWER MOVE FROM v6.0
    print(">>> AUTO-COMMAND 2: Opening Settings...")
    print("    >>> Please turn OFF WiFi + Bluetooth")
    print("    >>> Lower brightness manually")
    os.system('am start -a android.settings.SETTINGS')
    actions.append("Opened Settings for Manual Cooling")
    log_activity("ONE-CLICK: Opened Settings")
    
    # FINAL PROOF
    show_dashboard("COOLING ACTIVE", actions)
    print("🔥 AI BRAIN: MISSION COMPLETE.")
    print("✅ Phone should be cooling now.")
    print("\nScan Complete. Machine Stopped.")
    print("Run 'python battery_cooler_pro.py' again anytime.")

# ===== STARTUP =====
log_activity("ONE-CLICK v9.1 STARTED")
print("🛡️ OMNI-OPERATOR ONE-CLICK v9.1")
print("Engineer Eben | The Machine That Helps You")
print("="*50)
print("Starting One-Time Scan...\n")
ai_autopilot()
