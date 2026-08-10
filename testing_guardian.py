import os
import subprocess

class TestingGuardian:
    def __init__(self):
        self.name = "TESTING GUARDIAN v15.2"
    
    def test(self):
        print(f"\n[6/6] {self.name}")
        print("="*60)
        print("Scanning for tests...")
        
        if os.path.exists('test_') or os.path.exists('tests/'):
            print("[PYTEST] Found test files. Running...")
            result = subprocess.run("python -m pytest -v", shell=True)
            if result.returncode == 0:
                print("[SUCCESS] All tests passed. Code is safe to deploy.")
            else:
                print("[WARNING] Some tests failed. Fix before deploying.")
        else:
            print("[INFO] No tests found. Creating basic test file...")
            with open('test_basic.py', 'w') as f:
                f.write("def test_import():\n    import omni_orchestrator\n    assert omni_orchestrator\n")
            print("[SUCCESS] test_basic.py created. Run 'pytest' to test.")

if __name__ == "__main__":
    TestingGuardian().test()
