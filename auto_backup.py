import shutil
import datetime
import os

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_folder = f"backup_{timestamp}"

os.mkdir(backup_folder)
for file in os.listdir():
    if file.endswith(".py"):
        shutil.copy(file, backup_folder)

print(f"✅ Backup complete: {backup_folder}")
print("All .py files secured, Engineer Eben")
