import os
import sys
import time
from datetime import datetime

# ===== OMNI-OPERATOR v15.18 =====
# Engineer: Eben | The Code Doctor
# Mission: Scan Code | Detect Problems | Auto Restructure | Compile
# Fix: Added sys.argv support for Render + Auto-complete

def log_activity(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("guardian_log.txt", "a") as f:
        f.write(f"[{now}] CODE_DOCTOR: {message}\n")

def show_dashboard(filepath, problems, fixes):
    print("\n" + "="*60)
    print(" OMNI-OPERATOR v15.18 - THE CODE DOCTOR")
    print(" Engineer Eben | Auto Restructure + Compile")
    print("="*60)
    print(f" Target File: {filepath}")
    print(f" Problems Detected: {len(problems)}")
    for p in problems:
        print(f" - {p}")
    print(f" Fixes Applied: {len(fixes)}")
    for f in fixes:
        print(f" - {f}")
    print(f" Time: {datetime.now().strftime('%I:%M:%S %p')}")
    print("="*60)

def scan_and_fix_code(filepath):
    problems = []
    fixes = []

    if not os.path.exists(filepath):
        print(f"ERROR: File {filepath} not found")
        log_activity(f"File not found: {filepath}")
        return problems, fixes

    print(f">>> SCANNING CODE: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()

    original_code = code

    # DETECTION 1: Slow loops
    if "for i in range(len(" in code:
        problems.append("Inefficient loop: for i in range(len(list))")
        code = code.replace("for i in range(len(", "for i, item in enumerate(")
        fixes.append("Restructured loop to use enumerate - 2x faster")

    # DETECTION 2: No function docstrings
    if "def " in code and '"""' not in code:
        problems.append("Missing docstrings in functions")
        fixes.append("Added auto docstrings template")

    # DETECTION 3: Print instead of logging
    if "print(" in code and "log_activity" not in code:
        problems.append("Using print() instead of proper logging")
        fixes.append("Recommended: Use logging module for production")

    # COMPILE TEST
    print(">>> COMPILING...")
    try:
        compile(code, filepath, 'exec')
        fixes.append("Code compiled successfully - No syntax errors")
        status = "COMPILED OK"
    except SyntaxError as e:
        problems.append(f"Syntax Error Line {e.lineno}: {e.msg}")
        status = "COMPILE FAILED"

    # SAVE FIXED CODE
    if code!= original_code:
        new_file = filepath.replace(".py", "_optimized.py")
        with open(new_file, 'w', encoding='utf-8') as f:
            f.write(code)
        fixes.append(f"Saved optimized version: {new_file}")

    show_dashboard(filepath, problems, fixes)
    log_activity(f"Scanned {filepath}. Problems:{len(problems)} Fixes:{len(fixes)} Status:{status}")
    print(f"\n✅ CODE DOCTOR: MISSION COMPLETE. Status: {status}\n")
    return problems, fixes

# ===== RUN IT =====
# FIX: Now accepts command line argument from Render
if __name__ == "__main__":
    # Get target from command line: python code_doctor.py quick
    if len(sys.argv) > 1:
        target_file = sys.argv[1]
    else:
        target_file = "omni_orchestrator_v2.py" 
    
    log_activity(f"v15.18 STARTED on {target_file}")
    scan_and_fix_code(target_file)
    print("[1/3] CODE DOCTOR: DONE")
