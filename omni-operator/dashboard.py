from flask import Flask, render_template_string, request
import subprocess
import os
import datetime

app = Flask(__name__)

VERSION = "v15.23"
ENGINEER = "Engineer Eben"

HTML = f"""
<!DOCTYPE html>
<html>
<head>
<title>OMNI-OPERATOR {VERSION}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{{background:#0a0a0a;color:#00ff00;font-family:'Courier New', monospace;text-align:center;padding:20px;margin:0}}
.container{{max-width:900px;margin:auto}}
h1{{color:#00ff00;text-shadow:0 0 15px #00ff00;font-size:28px;margin:10px}}
h3{{color:#00cc00;margin:5px}}
.box{{border:2px solid #00ff00;border-radius:10px;padding:20px;margin:20px 0;background:#111}}
button{{background:#00ff00;color:#000;border:none;padding:15px 40px;font-size:18px;cursor:pointer;border-radius:5px;font-weight:bold}}
button:hover{{background:#00cc00;box-shadow:0 0 10px #00ff00}}
input{{padding:12px;width:80%;max-width:400px;background:#000;color:#00ff00;border:2px solid #00ff00;border-radius:5px;font-size:16px}}
pre{{text-align:left;background:#000;padding:20px;border-radius:5px;white-space:pre-wrap;border:1px solid #00ff00;max-height:500px;overflow-y:auto}}
.footer{{color:#555;font-size:12px;margin-top:20px}}
.status{{color:#00ffff}}
</style>
</head>
<body>
<div class="container">
<div class="box">
<h1>OMNI-OPERATOR {VERSION}</h1>
<h3>{ENGINEER} | Code Doctor + Security Guardian + Solidity Auditor</h3>
<p class="status">The Fully-Local AI DevOps Engine | Deployed on Render</p>
</div>

<form method="POST">
<div class="box">
<label><b>TARGET FOLDER:</b></label><br><br>
<input name="target" placeholder="Enter folder path or ." value=".">
<br><br>
<button name="action" value="run">RUN ORCHESTRATION</button>
</div>
</form>

<div class="box">
<h3>>> MISSION LOG <<</h3>
<pre>{{{{ output | safe }}}}</pre>
</div>

<div class="footer">
OMNI-OPERATOR {VERSION} | {datetime.datetime.now().strftime("%Y-%m-%d")}
</div>
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    output = f"Status: IDLE. Click RUN to start Omni-Operator {VERSION}..."
    if request.method == "POST":
        target = request.form.get("target", ".")
        output = f">>> OMNI-OPERATOR {VERSION} ACTIVATED <<<\n"
        output += f">>> TARGET: {target}\n"
        output += f">>> TIME: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        try:
            # RUN ALL 3 ROBOTS IN SEQUENCE
            result = subprocess.run(
                ["python", "omni_orchestrator_v2.py"], 
                input=target, 
                capture_output=True, 
                text=True,
                timeout=240  # 4 minutes for Render
            )
            output += result.stdout + result.stderr
            output += f"\n\n>>> MISSION COMPLETE. STATUS: SUCCESS <<<"
        except subprocess.TimeoutExpired:
            output += "\n\n[ERROR] Orchestration timed out after 4 minutes. Render free tier limit."
        except Exception as e:
            output += f"\n\n[CRITICAL ERROR] {str(e)}"
    return render_template_string(HTML, output=output)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # RENDER FIX
    app.run(host="0.0.0.0", port=port)
