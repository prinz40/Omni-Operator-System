import os
import glob
from datetime import datetime

# ===== OMNI-OPERATOR v14.1 =====
# Engineer: Eben | The Industry Robot - Directory Walker Edition
# =================================

def log_activity(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("guardian_log.txt", "a") as f:
        f.write(f"[{now}] ORCHESTRATOR: {message}\n")

def run_module(module, target):
    print(f"\n>>> RUNNING {module} on {target}")
    os.system(f"python {module} <<< '{target}'")

def omni_orchestrate():
    os.system('clear')
    print("="*60)
    print(" 🤖 OMNI-OPERATOR v14.1 - THE INDUSTRY ROBOT")
    print(" Engineer Eben | Walks Directories + Fixes All")
    print("="*60)
    
    target = input("Enter project folder or file to fix: ")
    log_activity(f"v14.1 ORCHESTRATION STARTED on {target}")
    
    # THE FIX: Find all files first
    files_to_scan = []
    if os.path.isdir(target):
        files_to_scan.extend(glob.glob(os.path.join(target, "**/*.py"), recursive=True))
        files_to_scan.extend(glob.glob(os.path.join(target, "**/*.sol"), recursive=True))
    else:
        files_to_scan.append(target)
    
    if not files_to_scan:
        print("No .py or .sol files found.")
        return
    
    print(f"\nFound {len(files_to_scan)} files to process.")
    
    for file in files_to_scan:
        print("\n" + "-"*40)
        print(f"PROCESSING: {file}")
        print("-"*40)
        
        print("\n[1/3] CODE DOCTOR")
        run_module("code_doctor.py", file)
        
        print("\n[2/3] SECURITY GUARDIAN")
        run_module("security_guardian.py", file)
        
        if file.endswith(".sol"):
            print("\n[3/3] SOLIDITY AUDITOR")
            run_module("solidity_auditor.py", file)
    
    print("\n[4/4] STAGE 4: AUTO COMMIT")
    os.system("git add . && git commit -m 'Omni Auto-Fix by Eben v14.1'")
    
    print("\n" + "="*60)
    print("🔥 ORCHESTRATION COMPLETE.")
    print(f"Machine scanned and fixed {len(files_to_scan)} files.")
    print("="*60)

omni_orchestrate()
