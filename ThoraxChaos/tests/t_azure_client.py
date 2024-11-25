# test_azure_client.py

import unittest
from unittest.mock import patch, MagicMock
from chaos_engine.azure_client import init_azure_clients

class TestAzureClient(unittest.TestCase):

    @patch('azure.mgmt.compute.ComputeManagementClient')
    @patch('azure.mgmt.network.NetworkManagementClient')
    @patch('azure.mgmt.resource.ResourceManagementClient')
    def test_init_azure_clients(self, MockResourceClient, MockNetworkClient, MockComputeClient):
        # Mock the Azure SDK clients
        mock_compute = MagicMock()
        mock_network = MagicMock()
        mock_resource = MagicMock()
        
        MockComputeClient.return_value = mock_compute
        MockNetworkClient.return_value = mock_network
        MockResourceClient.return_value = mock_resource
        
        subscription_id = "dummy-subscription-id"
        compute_client, network_client, resource_client = init_azure_clients(subscription_id)
        
        # Check if the clients are correctly initialized
        self.assertEqual(compute_client, mock_compute)
        self.assertEqual(network_client, mock_network)
        self.assertEqual(resource_client, mock_resource)

if __name__ == '__main__':
    unittest.main()
