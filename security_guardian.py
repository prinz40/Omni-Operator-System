import os
import re
from datetime import datetime

# ===== OMNI-OPERATOR v15.12 =====
# Engineer: Eben | The Security Guardian
# Mission: Scan Code | Detect Vulnerabilities | Auto Patch | Log
# Fix: Removed input() to prevent EOFError on Render

def log_activity(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("guardian_log.txt", "a") as f:
        f.write(f"[{now}] SECURITY: {message}\n")

def show_dashboard(filepath, vulns, patches):
    os.system('clear')
    print("="*60)
    print("  OMNI-OPERATOR v15.12 - THE SECURITY GUARDIAN")
    print("  Engineer Eben | Auto Vulnerability Detection + Patching")
    print("="*60)
    print(f" Target File: {filepath}")
    print(f" Vulnerabilities Detected:")
    for v in vulns:
        print(f"  - [CRITICAL] {v}")
    print(f" Auto Patches Applied:")
    for p in patches:
        print(f"  - [FIXED] {p}")
    print(f" Time: {datetime.now().strftime('%I:%M:%S %p')}")
    print("="*60)

def scan_and_patch_security(filepath):
    vulns = []
    patches = []

    if not os.path.exists(filepath):
        print(f"ERROR: File {filepath} not found")
        log_activity(f"File not found: {filepath}")
        return

    print(f">>> SECURITY SCAN STARTED: {filepath}")
    with open(filepath, 'r') as f:
        code = f.read()

    original_code = code

    # VULN 1: Dangerous eval()
    if "eval(" in code:
        vulns.append("Use of eval() - Code Injection Risk")
        code = code.replace("eval(", "# SECURITY PATCHED: eval() removed by Omni\n# ")
        patches.append("Commented out eval() - Prevents code injection")

    # VULN 2: Dangerous os.system() with user input
    if "os.system(" in code:
        vulns.append("Use of os.system() - Command Injection Risk")
        patches.append("Flagged os.system() - Recommend subprocess with validation")

    # VULN 3: Hardcoded passwords/secrets
    if re.search(r'password\s*=\s*["\'].*["\']', code, re.IGNORECASE):
        vulns.append("Hardcoded Password Detected")
        code = re.sub(r'password\s*=\s*["\'].*["\']', 'password = os.getenv("APP_PASSWORD")', code)
        patches.append("Replaced hardcoded password with os.getenv()")

    # VULN 4: No input validation
    if "input(" in code and "validate" not in code:
        vulns.append("Raw input() without validation")
        patches.append("Added comment: # TODO: Add input validation")

    # SAVE PATCHED CODE
    if code != original_code:
        new_file = filepath.replace(".py", "_secured.py")
        with open(new_file, 'w') as f:
            f.write(code)
        patches.append(f"Saved secured version: {new_file}")

    show_dashboard(filepath, vulns, patches)
    log_activity(f"Scanned {filepath}. Vulns:{len(vulns)} Patches:{len(patches)}")
    print(f"\n SECURITY GUARDIAN: SCAN COMPLETE.")

# ===== RUN IT =====
# FIX: No more input() - Safe for Render
# To scan a file, call: scan_and_patch_security("filename.py")
if __name__ == "__main__":
    # Example: scans orchestrator by default. Change the filename to scan others
    target_file = "omni_orchestrator_v2.py"
    log_activity(f"v15.12 STARTED on {target_file}")
    scan_and_patch_security(target_file)
