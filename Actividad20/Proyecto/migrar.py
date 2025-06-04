import os
import json
import subprocess

# 1. Leer config.cfg
config = {}
with open('legacy/config.cfg') as f:
    for line in f:
        if '=' in line:
            key, value = line.strip().split('=')
            config[key] = value

port = config.get('PORT', 'unknown')

# 2. Generar network.tf.json
network_tf = {
    "resource": {
        "null_resource": {
            "network": {
                "triggers": {
                    "port": port
                }
            }
        }
    }
}

with open('network.tf.json', 'w') as f:
    json.dump(network_tf, f, indent=2)

# 3. Generar main.tf.json
main_tf = {
    "resource": {
        "null_resource": {
            "local_server": {
                "provisioner": {
                    "local-exec": {
                        "command": f"echo 'Arrancando {port}'"
                    }
                },
                "triggers": {
                    "port": port
                }
            }
        }
    }
}

with open('main.tf.json', 'w') as f:
    json.dump(main_tf, f, indent=2)

# 4. Ejecutar terraform plan
print("✅ Archivos generados. Ejecutando terraform plan...\n")
subprocess.run(["terraform", "init", "-input=false"])
subprocess.run(["terraform", "plan"])
