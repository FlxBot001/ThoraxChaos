# cli.py

import argparse
from .experiment import chaos_experiment
from .config import load_config
from .report import generate_report

def terminate_experiment():
    """Handle the termination command of the chaos experiment."""
    print("Terminating the chaos experiment...")
    # Logic to terminate experiment (e.g., clean-up operations or stopping running failures)
    
def rebase_experiment():
    """Handle the rebase command to reset the experiment or reconfigure settings."""
    print("Rebasing the chaos experiment...")
    # Logic to reset the experiment or reconfigure
    config = load_config()
    chaos_experiment(config)

def parse_args():
    """Parse the command-line arguments."""
    parser = argparse.ArgumentParser(description="Chaos Engineering Simulation")
    parser.add_argument('--terminate', action='store_true', help="Terminate the chaos experiment")
    parser.add_argument('--rebase', action='store_true', help="Rebase the chaos experiment")
    parser.add_argument('--experiment', action='store_true', help="Run the chaos experiment")
    return parser.parse_args()

def cli():
    """Main CLI handler for chaos engineering."""
    args = parse_args()
    
    if args.terminate:
        terminate_experiment()
    elif args.rebase:
        rebase_experiment()
    elif args.experiment:
        config = load_config()
        chaos_experiment(config)
    else:
        print("No valid option selected. Use --help for usage information.")
