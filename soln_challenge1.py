import yaml
from pathlib import Path

# Define the ACI config structure
aci_challenge_config = {
    "tenant": "Tenant_CHG2",
    "vrf": "VRF_CHG2",
    "bridge_domain": {
        "name": "BD_CHG2",
        "subnet": "10.1.1.1/24",
        "advertise_externally": True
    },
    "application_profiles": [
        {
            "name": "APP1",
            "epgs": [
                {
                    "name": "EPG1",
                    "bd": "BD_CHG2",
                    "mode": "AEP",
                    "physical_domain": "PhysDmn1",
                    "vlan": 101
                },
                {
                    "name": "EPG3",
                    "bd": "BD_CHG2",
                    "mode": "static",
                    "static_path": {
                        "leaf": 102,
                        "port": "Eth1/1",
                        "vlan": 102
                    }
                }
            ]
        },
        {
            "name": "APP2",
            "epgs": [
                {
                    "name": "EPG2",
                    "bd": "BD_CHG2",
                    "mode": "static",
                    "static_path": {
                        "leaf": 101,
                        "ports": ["Eth1/1", "Eth1/2"],
                        "vlan": 100
                    }
                }
            ]
        }
    ],
    "contracts": [
        {
            "name": "Contract-EPG1-EPG2",
            "consumer": "EPG1",
            "provider": "EPG2"
        },
        {
            "name": "Contract-EPG1-EPG3",
            "consumer": "EPG1",
            "provider": "EPG3"
        }
    ]
}

# Write to YAML file
yaml_file = Path("/mnt/data/aci_config_challenge.yaml")
with open(yaml_file, "w") as f:
    yaml.dump(aci_challenge_config, f, sort_keys=False)

yaml_file.name
