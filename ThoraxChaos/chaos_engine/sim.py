# experiment.py

from .core import random_failure
from .azure_client import init_azure_clients
from .config import load_config
from .report import generate_report
import random

def chaos_experiment(config):
    """Main chaos experiment function that runs failure simulations on resources."""
    subscription_id = config['azure_subscription_id']
    compute_client, network_client, resource_client = init_azure_clients(subscription_id)
    
    success_count = 0
    failure_count = 0
    
    for resource in config['resources']:
        for failure in config['failures']:
            try:
                random_failure(config['failures'], resource, compute_client, network_client)
                success_count += 1
            except Exception as e:
                print(f"Failed to simulate {failure['type']} for {resource['name']}: {e}")
                failure_count += 1

    # After experiment completes, generate the report
    report_file = config['experiment_settings']['report_file']
    generate_report(success_count, failure_count, report_file)
