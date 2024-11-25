# test_cli.py

import unittest
from unittest.mock import patch
from chaos_engine.cli import cli, terminate_experiment, rebase_experiment

class TestCLI(unittest.TestCase):

    @patch('chaos_engine.cli.terminate_experiment')
    def test_terminate(self, mock_terminate):
        # Simulate the --terminate flag
        with patch('sys.argv', ['cli.py', '--terminate']):
            cli()
            mock_terminate.assert_called()

    @patch('chaos_engine.cli.rebase_experiment')
    def test_rebase(self, mock_rebase):
        # Simulate the --rebase flag
        with patch('sys.argv', ['cli.py', '--rebase']):
            cli()
            mock_rebase.assert_called()

    @patch('chaos_engine.cli.chaos_experiment')
    def test_experiment(self, mock_experiment):
        # Simulate the --experiment flag
        with patch('sys.argv', ['cli.py', '--experiment']):
            cli()
            mock_experiment.assert_called()

if __name__ == '__main__':
    unittest.main()
