# azure_client.py

from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient

def init_azure_clients(subscription_id):
    """Initialize Azure SDK clients for compute and network."""
    credential = DefaultAzureCredential()
    
    compute_client = ComputeManagementClient(credential, subscription_id)
    network_client = NetworkManagementClient(credential, subscription_id)
    resource_client = ResourceManagementClient(credential, subscription_id)
    
    return compute_client, network_client, resource_client
