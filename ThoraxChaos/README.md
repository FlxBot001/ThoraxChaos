Here's a comprehensive README for your chaos engineering simulation project. It includes setup instructions, usage details, and testing guidelines.

---

# Chaos Engineering Simulation for Azure

This project simulates chaos engineering experiments on Azure, allowing you to test system resilience by injecting failures into your Azure resources like virtual machines (VMs), networks, and more. You can simulate failures such as VM shutdowns, network latency, and CPU stress, orchestrate experiments, generate reports, and analyze the results.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [How to Use](#how-to-use)
- [Testing](#testing)
- [License](#license)

---

## Project Structure

```plaintext
chaos_engine/
├── __init__.py                       # Initialize the chaos engine module
├── core.py                           # Core functions for simulating failures
├── failure_simulation.py             # Simulate different failures (VM shutdown, network latency, etc.)
├── experiment_orchestrator.py        # Orchestrate the chaos experiments
├── azure_resources.py                # Manage Azure resources (VMs, networks, etc.)
├── report.py                         # Report generation logic
├── cli.py                            # CLI for managing experiments (start, terminate, rebase)
├── analytics.py                      # Analyze and report results of the chaos experiment
└── config.py                         # Load configuration settings

config/
├── config.yaml                       # Configuration for chaos experiments
└── config_template.yaml              # Template config file

logs/
└── chaos_experiment.log              # Log file for recording chaos experiment actions

reports/
└── experiment_report.json            # Experiment results in JSON format
└── experiment_report.html            # Human-readable experiment report in HTML format

tests/
├── test_failure_simulation.py        # Unit tests for failure simulation
├── test_experiment_orchestrator.py   # Unit tests for experiment orchestration
├── test_azure_resources.py           # Unit tests for Azure resource management
└── test_cli.py                       # Unit tests for CLI

analytics/
└── analytics.py                      # Analyze and visualize chaos experiment data
```

---

## Installation

To get started, you need to install the required dependencies for the project.

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/chaos-engine.git
   cd chaos-engine
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # For macOS/Linux
   venv\Scripts\activate      # For Windows
   ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Azure SDK Authentication**:
   You must authenticate with Azure using your Azure credentials. Ensure that you have set up authentication as per [Azure SDK Authentication documentation](https://learn.microsoft.com/en-us/python/api/azure-identity/azure.identity?view=azure-python).

---

## Configuration

Before running the chaos experiments, configure your settings in the `config/config.yaml` file. Here's an example configuration:

```yaml
chaos_experiment:
  failure_types:
    - vm_shutdown
    - network_latency
    - cpu_stress
  resources:
    resource_group: "rg-chaos-test"
    vm_name: "vm-test"
  duration: 120  # in seconds
  retries: 3

azure:
  subscription_id: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
  client_id: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
  tenant_id: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
  client_secret: "xxxxxxxxxxxxxxxxx"
```

- **failure_types**: A list of failure types you want to simulate (`vm_shutdown`, `network_latency`, `cpu_stress`).
- **resources**: The Azure resource group and VM names for simulation.
- **duration**: Duration of the experiment in seconds.
- **azure credentials**: Your Azure subscription and authentication details for accessing Azure resources.

---

## How to Use

### 1. **Start a Chaos Experiment**

To start a chaos experiment, use the CLI to run a failure simulation. For example:

```bash
python chaos_engine/cli.py start_experiment "vm_shutdown_test"
```

This command will start an experiment where the system will simulate the failure type specified in the configuration file (e.g., VM shutdown).

### 2. **Terminate the Chaos Experiment**

To terminate the running experiment (e.g., stop all simulations or revert changes), use the following command:

```bash
python chaos_engine/cli.py terminate_experiment
```

### 3. **Rebase the Chaos Experiment**

If you want to reset the experiment (for example, restart or clean up resources), use this command:

```bash
python chaos_engine/cli.py rebase_experiment
```

### 4. **Generate Reports**

After completing the chaos experiment, reports will be automatically generated. You can find them in the `reports/` directory:
- `experiment_report.json`: A detailed report in JSON format.
- `experiment_report.html`: A human-readable report in HTML format.

---

## Testing

### Unit Tests

The project includes unit tests for failure simulation, experiment orchestration, Azure resource management, and the CLI.

1. **Run Unit Tests**:

   To run all the unit tests, simply execute the following command:

   ```bash
   pytest tests/
   ```

2. **Test Failure Simulation**:
   
   Tests for simulating failures like VM shutdown, network latency, and CPU stress can be found in `tests/test_failure_simulation.py`.

   ```bash
   python tests/test_failure_simulation.py
   ```

3. **Test Experiment Orchestration**:

   The orchestration logic is tested in `tests/test_experiment_orchestrator.py`. You can run it using:

   ```bash
   python tests/test_experiment_orchestrator.py
   ```

4. **Test Azure Resource Management**:

   Ensure your Azure resources are correctly managed by running the tests in `tests/test_azure_resources.py`:

   ```bash
   python tests/test_azure_resources.py
   ```

5. **Test CLI Commands**:

   To test the CLI commands (start, terminate, rebase), run the following tests:

   ```bash
   python tests/test_cli.py
   ```

---

## Analytics

Once your chaos experiment completes, you can analyze the results using the `analytics.py` module, which processes the generated reports and gives you insights such as the success rate of the simulations, failure patterns, and resource impact.

To analyze the experiment data:

```bash
python analytics/analytics.py --report reports/experiment_report.json
```

This command will process the results and provide statistical insights into the chaos experiment.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

By following these instructions, you should be able to successfully configure, simulate, and analyze chaos engineering experiments on your Azure resources.