# test_report.py

import unittest
from unittest.mock import patch
from chaos_engine.report import generate_report

class TestReportGeneration(unittest.TestCase):

    @patch('builtins.open', create=True)
    def test_generate_report(self, mock_open):
        # Test the report generation functionality
        success_count = 5
        failure_count = 2
        report_file = 'test_report.json'

        generate_report(success_count, failure_count, report_file)

        # Check if the file was opened in write mode
        mock_open.assert_called_with(report_file, 'w')

        # Check if the report was generated correctly
        mock_open.return_value.write.assert_called_once_with(
            '{"total_simulations": 7, "successes": 5, "failures": 2, "success_percentage": 71.42857142857143, "failure_percentage": 28.57142857142857}\n'
        )

if __name__ == '__main__':
    unittest.main()
