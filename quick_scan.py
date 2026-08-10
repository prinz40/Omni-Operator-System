import subprocess
import os

print("OMNI-OPERATOR v15.15 QUICK SCAN")
print("Scanning 5 files only to avoid Render timeout")

files = os.listdir('.')[:5]  # Only first 5 files
for f in files:
    if f.endswith('.py'):
        print(f"SCANNING: {f}")
        subprocess.run(["python", "omni_operator.py", f])

print("✅ QUICK SCAN COMPLETE - EVIDENCE READY")
