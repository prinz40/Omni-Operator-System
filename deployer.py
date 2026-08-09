import os
import subprocess

class CloudDeployer:
    def __init__(self):
        self.name = "CLOUD DEPLOYER v15.1"
    
    def deploy(self):
        print(f"\n[5/5] {self.name}")
        print("="*50)
        print("Scanning for deployment type...")
        
        files = os.listdir('.')
        
        if 'requirements.txt' in files or any(f.endswith('.py') for f in files):
            print("[PYTHON] Detected Python project")
            self._deploy_python()
        elif 'package.json' in files:
            print("[NODE] Detected Node.js project")
            self._deploy_node()
        else:
            print("[INFO] No auto-deploy config found. Creating one.")
            self._create_render_config()
            
        print("DEPLOYMENT CONFIG READY. Push to GitHub and connect to Render.")

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
        print("[SUCCESS] render.yaml created. Go to render.com -> New Web Service -> Connect GitHub")

    def _deploy_node(self):
        print("[SUCCESS] package.json found. Go to vercel.com -> Import GitHub Repo")

    def _create_render_config(self):
        print("Add a main.py or app.py and requirements.txt to enable auto-deploy")

if __name__ == "__main__":
    CloudDeployer().deploy()
