import unittest
from chaos_engine.experiment_orchestrator import run_experiment
from chaos_engine.failure_simulation import simulate_vm_shutdown

class TestExperimentOrchestrator(unittest.TestCase):
    def test_run_experiment(self):
        config = {
            'chaos_experiment': {
                'failure_types': ['vm_shutdown']
            }
        }
        run_experiment(config)

if __name__ == '__main__':
    unittest.main()
