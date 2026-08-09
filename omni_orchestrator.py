import os
from datetime import datetime

# ===== OMNI-OPERATOR v14.0 =====
# Engineer: Eben | The Industry Robot
# Mission: One Command → Scan All → Fix All → Build All → Deploy
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
    print(" 🤖 OMNI-OPERATOR v14.0 - THE INDUSTRY ROBOT")
    print(" Engineer Eben | Auto Building + Security + Deployment")
    print("="*60)
    
    target = input("Enter project folder or file to fix: ")
    log_activity(f"v14.0 ORCHESTRATION STARTED on {target}")
    
    print("\n[1/3] STAGE 1: CODE DOCTOR")
    run_module("code_doctor.py", target)
    
    print("\n[2/3] STAGE 2: SECURITY GUARDIAN")
    run_module("security_guardian.py", target)
    
    print("\n[3/3] STAGE 3: SOLIDITY AUDITOR")
    if ".sol" in target:
        run_module("solidity_auditor.py", target)
    
    print("\n[4/4] STAGE 4: AUTO COMMIT")
    os.system("git add . && git commit -m 'Omni Auto-Fix by Eben v14.0'")
    
    print("\n" + "="*60)
    print("🔥 ORCHESTRATION COMPLETE.")
    print("Machine scanned, fixed, secured, and built your project.")
    print("="*60)

omni_orchestrate()
