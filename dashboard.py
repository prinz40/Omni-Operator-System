from flask import Flask, render_template_string, request
import subprocess
import os

app = Flask(__name__)

VERSION = "v15.11"

HTML = f"""
<!DOCTYPE html>
<html>
<head><title>OMNI-OPERATOR {VERSION}</title>
<style>
body{{background:#0a0a0a;color:#00ff00;font-family:monospace;text-align:center;padding:50px}}
h1{{color:#00ff00;text-shadow:0 0 10px #00ff00}}
button{{background:#00ff00;color:#000;border:none;padding:15px 40px;font-size:18px;cursor:pointer;border-radius:5px}}
button:hover{{background:#00cc00}}
input{{padding:10px;width:300px;background:#111;color:#00ff00;border:1px solid #00ff00}}
pre{{text-align:left;background:#111;padding:20px;border-radius:5px;white-space:pre-wrap}}
</style>
</head>
<body>
<h1>OMNI-OPERATOR {VERSION}</h1>
<h3>Engineer Eben | The Industry Robot</h3>
<form method="POST">
<input name="target" placeholder="Enter folder or ." value=".">
<br><br>
<button name="action" value="run">RUN ORCHESTRATION</button>
</form>
<pre>{'{{ output | safe }}'}</pre>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    output = "Click RUN to start Omni-Operator..."
    if request.method == "POST":
        target = request.form.get("target", ".")
        output = f">>> RUNNING ORCHESTRATION ON: {target}\n\n"
        try:
            # FIX: timeout so Render doesn't kill it. 120s max
            result = subprocess.run(
                ["python", "omni_orchestrator_v2.py"], 
                input=target, 
                capture_output=True, 
                text=True,
                timeout=120
            )
            output += result.stdout + result.stderr
        except subprocess.TimeoutExpired:
            output += "\n\n[ERROR] Orchestration took longer than 2 minutes. Render free tier timed out.\nRun on smaller folder or upgrade Render."
        except Exception as e:
            output += f"\n\n[ERROR] {str(e)}"
    return render_template_string(HTML, output=output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
