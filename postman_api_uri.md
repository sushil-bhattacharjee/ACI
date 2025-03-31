 https://chatgpt.com/c/67db9177-7588-800b-8d17-737f69e484c8
 1. Tenant Configuration
GET https://192.168.89.95/api/node/class/fvTenant.json

🔹 2. VRF Configuration (Context)
GET https://192.168.89.95/api/node/class/fvCtx.json

Or specific to your tenant:
GET https://192.168.89.95/api/node/mo/uni/tn-Tenant_CHG2.json?query-target=children&target-subtree-class=fvCtx

 3. EPG Configurations
 GET https://192.168.89.95/api/node/class/fvAEPg.json

Or per Application Profile (APP1, APP2):
GET https://192.168.89.95/api/node/mo/uni/tn-Tenant_CHG2/ap-APP1.json?query-target=children&target-subtree-class=fvAEPg
GET https://192.168.89.95/api/node/mo/uni/tn-Tenant_CHG2/ap-APP2.json?query-target=children&target-subtree-class=fvAEPg

🔹 4. Bridge Domain Configuration
GET https://192.168.89.95/api/node/class/fvBD.json

Or scoped by tenant:
GET https://192.168.89.95/api/node/mo/uni/tn-Tenant_CHG2.json?query-target=children&target-subtree-class=fvBD

