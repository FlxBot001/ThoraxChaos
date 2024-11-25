# test_experiment.py

import unittest
from unittest.mock import MagicMock, patch
from chaos_engine.experiment import chaos_experiment

class TestExperimentLogic(unittest.TestCase):

    @patch('chaos_engine.core.random_failure')
    @patch('chaos_engine.azure_client.init_azure_clients')
    @patch('chaos_engine.report.generate_report')
    def test_chaos_experiment(self, mock_generate_report, mock_init_azure_clients, mock_random_failure):
        # Setup mocks
        config = {
            'azure_subscription_id': 'dummy-subscription-id',
            'resources': [{'name': 'test-vm', 'region': 'eastus'}],
            'failures': [{'type': 'VMShutdown', 'probability': 1.0}],
            'experiment_settings': {'report_file': 'test_report.json'}
        }
        mock_compute_client = MagicMock()
        mock_network_client = MagicMock()
        mock_resource_client = MagicMock()

        mock_init_azure_clients.return_value = (mock_compute_client, mock_network_client, mock_resource_client)

        # Run the chaos experiment
        chaos_experiment(config)

        # Check if the random failure function was called
        mock_random_failure.assert_called()

        # Check if the report generation was triggered
        mock_generate_report.assert_called()

if __name__ == '__main__':
    unittest.main()
