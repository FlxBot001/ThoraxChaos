import yaml
from chaos_engine.failure_simulation import simulate_vm_shutdown, simulate_network_latency, simulate_cpu_stress

def load_config(config_path="config/config.yaml"):
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

def run_experiment(config):
    failure_types = config['chaos_experiment']['failure_types']
    
    for failure_type in failure_types:
        print(f"Starting failure simulation: {failure_type}")
        
        if failure_type == 'vm_shutdown':
            simulate_vm_shutdown()
        elif failure_type == 'network_latency':
            simulate_network_latency()
        elif failure_type == 'cpu_stress':
            simulate_cpu_stress()
        else:
            print(f"Unknown failure type: {failure_type}")
        
        print(f"Completed failure simulation: {failure_type}")
