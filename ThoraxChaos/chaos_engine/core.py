# core.py

import random

def simulate_failure(failure_type, resource, compute_client, network_client):
    """Simulate various failure scenarios on Azure resources."""
    
    if failure_type == 'VMShutdown':
        print(f"Simulating VM shutdown for {resource['name']} in {resource['region']}")
        try:
            # Azure SDK call to shutdown the VM (using the provided Azure client)
            compute_client.virtual_machines.power_off(resource['name'], resource['region'])
        except Exception as e:
            print(f"Error during VM shutdown: {e}")
            raise
    elif failure_type == 'NetworkDisruption':
        print(f"Simulating network disruption for {resource['name']} in {resource['region']}")
        try:
            # Example of network disruption, deallocate network interface
            network_client.network_interfaces.deallocate(resource['name'], resource['region'])
        except Exception as e:
            print(f"Error during network disruption: {e}")
            raise
    elif failure_type == 'DiskFailure':
        print(f"Simulating disk failure for {resource['name']} in {resource['region']}")
        try:
            # Simulate disk failure, this can be detaching a disk or some other logic
            pass
        except Exception as e:
            print(f"Error during disk failure: {e}")
            raise
    else:
        raise ValueError(f"Unsupported failure type: {failure_type}")
    
def random_failure(failures, resource, compute_client, network_client):
    """Randomly choose a failure based on probability."""
    failure = random.choice(failures)
    if random.random() < failure['probability']:
        simulate_failure(failure['type'], resource, compute_client, network_client)
