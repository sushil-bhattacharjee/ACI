import requests
import yaml
import json

# Disable SSL warnings
requests.packages.urllib3.disable_warnings()

# === CONFIG ===
APIC_URL = "https://192.168.89.95"
USERNAME = "admin"
PASSWORD = "97249_NEC"  # Replace with your APIC password

# === STEP 1: Login to APIC ===
login_url = f"{APIC_URL}/api/aaaLogin.json"
auth_payload = {
    "aaaUser": {
        "attributes": {
            "name": USERNAME,
            "pwd": PASSWORD
        }
    }
}

print("[+] Logging into APIC...")
session = requests.Session()
resp = session.post(login_url, json=auth_payload, verify=False)
if not resp.ok:
    print(f"[!] Login failed: {resp.status_code}")
    exit(1)

# === STEP 2: Get Full Config ===
config_url = f"{APIC_URL}/api/node/mo/uni.json?rsp-subtree=full&rsp-prop-include=config-only"
print("[+] Retrieving full APIC config...")

resp = session.get(config_url, verify=False)
if not resp.ok:
    print(f"[!] Failed to retrieve config: {resp.status_code}")
    exit(1)

apic_config_json = resp.json()

# === STEP 3: Convert to YAML ===
yaml_file = "apic_config_export.yml"
with open(yaml_file, 'w') as f:
    yaml.dump(apic_config_json, f, sort_keys=False)

print(f"[✓] APIC config saved to: {yaml_file}")
