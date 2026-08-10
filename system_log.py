from datetime import datetime

print("📊 OMNI-OPERATOR SYSTEM LOG")
now = datetime.now()
log_time = now.strftime("%Y-%m-%d %H:%M:%S")

log_entry = f"[{log_time}] Guardian Active | Battery ~59% | Status: Protecting\n"

with open("guardian_log.txt", "a") as f:
    f.write(log_entry)

print(f"Log saved: {log_entry}")
print("Check your logs with: cat guardian_log.txt")
