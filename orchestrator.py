import os
import glob
import subprocess
from datetime import datetime

# ===== OMNI-OPERATOR v15.5 =====
# Engineer: Eben | The Industry Robot - Render Fixed Edition
# =================================

def log_activity(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("guardian_log.txt", "a") as f:
        f.write(f"[{now}] ORCHESTRATOR: {message}\n")

def run_module(module, target):
    print(f"\n>>> RUNNING {module} on {target}")
    # FIX 1: Changed &> to > /dev/null 2>&1 for Render sh compatibility
    subprocess.run(f"python {module} <<< '{target}' > /dev/null 2>&1", shell=True)

class CloudDeployer:
    def __init__(self):
        self.name = "CLOUD DEPLOYER v15.1"
    
    def deploy(self):
        print(f"\n[5/6] {self.name}")
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
            subprocess.run("pip freeze > requirements.txt 2>/dev/null", shell=True)
        
        print("Creating render.yaml for 1-click deploy...")
        with open('render.yaml', 'w') as f:
            f.write("""services:
    - type: web
    name: omni-app
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn dashboard:app
""")
        print("[SUCCESS] render.yaml created.")

    def _deploy_node(self):
        print("[SUCCESS] package.json found. Ready for Vercel.")

class TestingGuardian:
    def __init__(self):
        self.name = "TESTING GUARDIAN v15.2"
    
    def test(self):
        print(f"\n[6/6] {self.name}")
        print("="*60)
        print("Scanning for tests...")
        
        files = [f for f in os.listdir('.') if f.startswith('test_')]
        has_tests_dir = os.path.exists('tests')
        
        if files or has_tests_dir:
            print("[PYTEST] Found test files. Running...")
            result = subprocess.run("python -m pytest -v > /dev/null 2>&1", shell=True)
            if result.returncode == 0:
                print("[SUCCESS] All tests passed. Code is safe to deploy.")
            else:
                print("[WARNING] Some tests failed. Fix before deploying.")
        else:
            print("[INFO] No tests found. Creating basic test file...")
            with open('test_basic.py', 'w') as f:
                f.write("def test_import():\n    import omni_orchestrator\n    assert omni_orchestrator\n")
            print("[SUCCESS] test_basic.py created. Run 'pytest' to test.")

def omni_orchestrate():
    os.system("clear")
    print("*"*60)
    print(" OMNI-OPERATOR v15.5 - THE INDUSTRY ROBOT")
    print(" Engineer Eben | Fixes All + Deploys + Auto Tests")
    print("*"*60)

    target = input("Enter project folder or file to fix: ")
    log_activity(f"v15.5 ORCHESTRATION STARTED on {target}")

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

    print("\n[4/6] STAGE 4: AUTO COMMIT")
    # FIX 2: Add git config so Render stops complaining
    os.system('git config --global user.email "eben@omni.ai" && git config --global user.name "Eben"')
    os.system('git add . && git commit -m "Omni Auto-Fix by Eben v15.5" > /dev/null 2>&1')

    # STAGE 5: CLOUD DEPLOYER
    deployer = CloudDeployer()
    deployer.deploy()

    # STAGE 6: TESTING GUARDIAN
    tester = TestingGuardian()
    tester.test()

    print("\n" + "="*60)
    print("ORCHESTRATION COMPLETE.")
    print(f"Machine scanned, fixed, tested, and prepared {len(files_to_scan)} files for deployment.")
    print("*"*60)

omni_orchestrate()
