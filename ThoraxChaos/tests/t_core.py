# test_core.py

import unittest
from unittest.mock import MagicMock
from chaos_engine.core import simulate_failure, random_failure

class TestCoreFunctions(unittest.TestCase):

    def setUp(self):
        # Mock Azure clients and resources
        self.compute_client = MagicMock()
        self.network_client = MagicMock()
        self.resource = {'name': 'test-vm', 'region': 'eastus'}

    def test_simulate_vm_shutdown(self):
        # Test the VM shutdown failure simulation
        simulate_failure('VMShutdown', self.resource, self.compute_client, self.network_client)
        self.compute_client.virtual_machines.power_off.assert_called_with(self.resource['name'], self.resource['region'])

    def test_simulate_network_disruption(self):
        # Test network disruption failure simulation
        simulate_failure('NetworkDisruption', self.resource, self.compute_client, self.network_client)
        self.network_client.network_interfaces.deallocate.assert_called_with(self.resource['name'], self.resource['region'])

    def test_random_failure(self):
        # Test random failure selection
        failures = [{'type': 'VMShutdown', 'probability': 0.5}, {'type': 'NetworkDisruption', 'probability': 0.5}]
        random_failure(failures, self.resource, self.compute_client, self.network_client)
        # We can't test randomness directly, but we can check that the correct functions were called
        self.compute_client.virtual_machines.power_off.assert_called_once()  # or the network disruption mock

if __name__ == '__main__':
    unittest.main()
