import random
from chaos_engine.azure_client import simulate_failure
import random

def simulate_random_failure(resource_group_name, resource_name):
    failure_types = ["vm_shutdown", "network_partition", "sql_failover"]
    failure_type = random.choice(failure_types)
    simulate_failure(failure_type, resource_group_name, resource_name)

def simulate_vm_shutdown():
    # Simulate a VM shutdown on Azure
    print("Simulating VM shutdown...")
    time.sleep(random.randint(1, 5))  # Random delay for shutdown simulation
    print("VM shutdown complete.")

def simulate_network_latency():
    # Simulate network latency by adding delay
    print("Simulating network latency...")
    time.sleep(random.randint(2, 6))  # Random delay to simulate latency
    print("Network latency simulation complete.")

def simulate_cpu_stress():
    # Simulate CPU stress by introducing heavy load
    print("Simulating CPU stress...")
    time.sleep(random.randint(3, 7))  # Random delay to simulate stress
    print("CPU stress simulation complete.")
