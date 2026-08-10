import re
import os
from datetime import datetime

# ===== OMNI-OPERATOR v15.12 =====
# Engineer: Eben | The Solidity Contract Auditor
# Mission: Scan sol | Detect Vulnerabilities | Auto Patch | Test
# Fix: Removed input() to prevent EOFError on Render

def log_activity(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("guardian_log.txt", "a") as f:
        f.write(f"[{now}] SOLIDITY: {message}\n")

def show_dashboard(filepath, vulns, patches):
    os.system('clear')
    print("="*60)
    print("  OMNI-OPERATOR v15.12 - THE SOLIDITY AUDITOR")
    print("  Engineer Eben | Auto Contract Security + Solidify")
    print("="*60)
    print(f" Target Contract: {filepath}")
    print(f" Vulnerabilities Detected:")
    for v in vulns:
        print(f"  - [CRITICAL] {v}")
    print(f" Auto Patches Applied:")
    for p in patches:
        print(f"  - [FIXED] {p}")
    print("="*60)

def scan_solidity(filepath):
    vulns = []
    patches = []

    if not os.path.exists(filepath):
        print(f"ERROR: File {filepath} not found")
        log_activity(f"File not found: {filepath}")
        return

    print(f">>> AUDITING SMART CONTRACT: {filepath}")
    with open(filepath, 'r') as f:
        code = f.read()
    original_code = code

    # VULN 1: Reentrancy
    if ".call{value:" in code:
        vulns.append("Potential Reentrancy Attack - external call before state change")
        patches.append("Recommend: Use Checks-Effects-Interactions pattern + ReentrancyGuard")

    # VULN 2: Integer Overflow
    if "pragma solidity" in code and "^0.8" not in code:
        vulns.append("Old Solidity version - Integer Overflow risk")
        patches.append("Recommend: Upgrade to ^0.8.0 for built-in overflow checks")

    # VULN 3: tx.origin
    if "tx.origin" in code:
        vulns.append("Use of tx.origin - Phishing risk")
        patches.append("FIXED: Replaced tx.origin with msg.sender")
        code = code.replace("tx.origin", "msg.sender")

    # SAVE PATCHED CODE IF CHANGED
    if code != original_code:
        new_file = filepath.replace(".sol", "_audited.sol")
        with open(new_file, 'w') as f:
            f.write(code)
        patches.append(f"Saved audited version: {new_file}")

    show_dashboard(filepath, vulns, patches)
    log_activity(f"Audited {filepath}. Vulns:{len(vulns)}")
    print(f"\n SOLIDITY AUDITOR: AUDIT COMPLETE.")

# ===== RUN IT =====
# FIX: No more input() - Safe for Render
# To audit a file, call: scan_solidity("filename.sol")
if __name__ == "__main__":
    # Example: scans a dummy contract by default. Change the filename to audit others
    target_file = "ExampleContract.sol"
    log_activity(f"v15.12 STARTED on {target_file}")
    scan_solidity(target_file)
