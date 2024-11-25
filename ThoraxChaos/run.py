import argparse
from chaos_engine.cli import run_cli  # Ensure the correct function is imported

def main():
    parser = argparse.ArgumentParser(description="Chaos Engineering Simulation")
    
    # Option to run the chaos experiment
    parser.add_argument('--experiment', action='store_true', help="Run the chaos experiment")
    parser.add_argument('--action', choices=['start', 'terminate', 'rebase', 'analyze'], help="Action to perform on chaos experiment")
    parser.add_argument('--experiment_name', type=str, help="Name of the chaos experiment", required=False)
    parser.add_argument('--report', type=str, help="Path to the experiment report for analysis", required=False)

    # Parse the command-line arguments
    args = parser.parse_args()

    # If --experiment is set, then pass control to the CLI
    if args.experiment:
        if args.action:
            # Run the CLI function with the appropriate arguments
            run_cli(args)
        else:
            print("You must specify an action (start, terminate, rebase, analyze).")
            exit(1)

if __name__ == "__main__":
    main()
