from flask import Flask, render_template_string, request
import subprocess
import os

app = Flask(__name__)

VERSION = "v15.10"

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
</style>
</head>
<body>
<h1>OMNI-OPERATOR {VERSION}</h1>
<h3>Engineer Eben | The Industry Robot</h3>
<form method="POST">
<input class="input" name="target" placeholder="Enter folder or ." value=".">
<br><br>
<button name="action" value="run">RUN ORCHESTRATION</button>
</form>
<pre style="text-align:left;background:#111;padding:20px;border-radius:5px;">{{ output }}}}</pre>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    output = ""
    if request.method == "POST":
        target = request.form["target"]
        # FIX: Removed shell pipe and echo. Direct python call for Render
        result = subprocess.run(["python", "omni_orchestrator_v2.py"], input=target, capture_output=True, text=True)
        output = result.stdout + result.stderr
    return render_template_string(HTML, output=output)

if __name__ == "__main__":
    print(f"Starting Dashboard on http://0.0.0.0:5000 - {VERSION}")
    app.run(host="0.0.0.0", port=5000)
