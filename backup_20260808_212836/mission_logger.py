import datetime

log = open("mission_log.txt", "a")
log.write(f"Mission executed at: {datetime.datetime.now()}\n")
log.write("Status: OMNI-OPERATOR completed task successfully\n")
log.write("Engineer: Eben\n\n")
log.close()

print("✅ Mission logged successfully")
print("Check file: mission_log.txt")
