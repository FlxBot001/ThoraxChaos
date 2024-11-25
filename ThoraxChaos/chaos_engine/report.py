# report.py

import json

def generate_report(success_count, failure_count, report_file):
    """Generate a detailed chaos experiment report and save it to a file."""
    total = success_count + failure_count
    success_percentage = (success_count / total) * 100 if total else 0
    failure_percentage = (failure_count / total) * 100 if total else 0
    
    report = {
        "total_simulations": total,
        "successes": success_count,
        "failures": failure_count,
        "success_percentage": success_percentage,
        "failure_percentage": failure_percentage
    }
    
    # Save the report as a JSON file
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=4)
    
    print(f"Report generated and saved to {report_file}")


import json
import os

def generate_report(experiment_results, report_file="reports/experiment_report.json"):
    with open(report_file, "w") as file:
        json.dump(experiment_results, file, indent=4)
    print(f"Experiment report saved to {report_file}")

def generate_html_report(experiment_results, report_file="reports/experiment_report.html"):
    with open(report_file, "w") as file:
        file.write("<html><body><h1>Chaos Experiment Report</h1>")
        file.write("<h2>Results</h2>")
        file.write(f"<p>{json.dumps(experiment_results, indent=4)}</p>")
        file.write("</body></html>")
    print(f"HTML report saved to {report_file}")
