from credentials import *
from acitoolkit import acitoolkit

# Connect to the APIC
session = acitoolkit.Session(URL, LOGIN, PASSWORD)
resp = session.login()

if not resp.ok:
    print(f"Login failed: {resp.status_code} - {resp.text}")
    exit()

# Define the tenant name
tenant_name = "INITIALS_Toolkit_Tenant"
new_tenant = acitoolkit.Tenant(tenant_name)

# Push the configuration
push_resp = session.push_to_apic(new_tenant.get_url(), new_tenant.get_json())

# Print result
if push_resp.ok:
    print(f"Tenant '{tenant_name}' created successfully.")
else:
    print(f"Failed to create tenant: {push_resp.status_code} - {push_resp.text}")
