from credentials import *
import cobra.mit.access
import cobra.mit.request
import cobra.mit.session
import cobra.model.fv
import cobra.model.pol

# connect to the apic
auth = cobra.mit.session.LoginSession(URL, LOGIN, PASSWORD)
session = cobra.mit.access.MoDirectory(auth)
session.login()
# <Response [200]> --> If you do not see this response the login did not work

# Create a Variable for your Tenant Name
# Use your initials in the name
# Example: tenant_name = "js_Cobra_Tenant"
tenant_name = "INITIALS_Cobra_Tenant"

# create a new tenant
root = cobra.model.pol.Uni('')
new_tenant = cobra.model.fv.Tenant(root, tenant_name)

# commit the new configuration
config_request = cobra.mit.request.ConfigRequest()
config_request.addMo(new_tenant)
session.commit(config_request)

# <Response [200]> --> If you do not see this response the tenant create did not wor