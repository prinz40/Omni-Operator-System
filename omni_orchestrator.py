import os
import glob
import subprocess
from datetime import datetime

# ===== OMNI-OPERATOR v15.1 =====
# Engineer: Eben | The Industry Robot - Cloud Deployer Edition
# =================================

def log_activity(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("guardian_log.txt", "a") as f:
        f.write(f"[{now}] ORCHESTRATOR: {message}\n")

def run_module(module, target):
    print(f"\n>>> RUNNING {module} on {target}")
    os.system(f"python {module} <<< '{target}'")

class CloudDeployer:
    def __init__(self):
        self.name = "CLOUD DEPLOYER v15.1"
    
    def deploy(self):
        print(f"\n[5/5] {self.name}")
        print("="*60)
        print("Scanning for deployment type...")
        
        files = os.listdir('.')
        
        if 'requirements.txt' in files or any(f.endswith('.py') for f in files):
            print("[PYTHON] Detected Python project")
            self._deploy_python()
        elif 'package.json' in files:
            print("[NODE] Detected Node.js project")
            self._deploy_node()
        else:
            print("[INFO] No auto-deploy config found.")
            
        print("DEPLOYMENT CONFIG READY. Push to GitHub and connect to Render.com")

    def _deploy_python(self):
        if 'requirements.txt' not in os.listdir('.'):
            print("Creating requirements.txt...")
            subprocess.run("pip freeze > requirements.txt", shell=True)
        
        print("Creating render.yaml for 1-click deploy...")
        with open('render.yaml', 'w') as f:
            f.write("""services:
    - type: web
    name: omni-app
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python app.py
""")
        print("[SUCCESS] render.yaml created.")

    def _deploy_node(self):
        print("[SUCCESS] package.json found. Ready for Vercel.")

def omni_orchestrate():
    os.system("clear")
    print("*"*60)
    print(" OMNI-OPERATOR v15.1 - THE INDUSTRY ROBOT")
    print(" Engineer Eben | Walks Directories + Fixes All + Deploys")
    print("*"*60)

    target = input("Enter project folder or file to fix: ")
    log_activity(f"v15.1 ORCHESTRATION STARTED on {target}")

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
        print("\n" + "="*40)
        print(f"PROCESSING: {file}")
        print("="*40)

        print("\n[1/3] CODE DOCTOR")
        run_module("code_doctor.py", file)

        print("\n[2/3] SECURITY GUARDIAN")
        run_module("security_guardian.py", file)

        if file.endswith(".sol"):
            print("\n[3/3] SOLIDITY AUDITOR")
            run_module("solidity_auditor.py", file)

    print("\n[4/4] STAGE 4: AUTO COMMIT")
    os.system('git add . && git commit -m "Omni Auto-Fix by Eben v15.1"')

    # STAGE 5: CLOUD DEPLOYER
    deployer = CloudDeployer()
    deployer.deploy()

    print("\n" + "="*60)
    print("ORCHESTRATION COMPLETE.")
    print(f"Machine scanned, fixed, and prepared {len(files_to_scan)} files for deployment.")
    print("*"*60)

omni_orchestrate()
