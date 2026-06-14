import pytest
from click.testing import CliRunner
from src.cli import calculate


class TestCLIIntegration:
    def setup_method(self):
        self.runner = CliRunner()

    def test_cli_add_integration(self):
        result = self.runner.invoke(calculate, ["add", "5", "3"])
        assert result.exit_code == 0
        assert result.output.strip() == "8"

    def test_cli_subtract_integration(self):
        result = self.runner.invoke(calculate, ["subtract", "5", "3"])
        assert result.exit_code == 0
        assert result.output.strip() == "2"

    def test_cli_subtract_missing_operand_error(self):
        result = self.runner.invoke(calculate, ["subtract", "5"])
        assert result.exit_code != 0
        assert "Unexpected error:" in result.output

    def test_cli_multiply_integration(self):
        result = self.runner.invoke(calculate, ["multiply", "5", "3"])
        assert result.exit_code == 0
        assert result.output.strip() == "15"

    def test_cli_divide_integration(self):
        result = self.runner.invoke(calculate, ["divide", "5", "3"])
        assert result.exit_code == 0
        assert result.output.strip() == "1.67"


class TestCLIErrorCases:
    def setup_method(self):
        self.runner = CliRunner()

    def test_cli_unknown_operation(self):
        result = self.runner.invoke(calculate, ["foobar", "5", "3"])
        assert result.exit_code == 1
        assert "Unknown operation" in result.output

    def test_cli_square_root_negative(self):
        result = self.runner.invoke(calculate, ["square_root", "-9"])
        assert result.exit_code == 2
