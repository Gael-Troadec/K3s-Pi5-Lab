import time
import platform

print("Demarrage du systeme Architeuthis...", flush=True)
print(f"Architeuthis detectee : {platform.machine()}", flush=True)

while True:
    print("En attente d'ordres...", flush=True)
    time.sleep(60)