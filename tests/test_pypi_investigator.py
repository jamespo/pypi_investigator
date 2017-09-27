#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pypi_investigator` package."""


import unittest
from click.testing import CliRunner

from pypi_investigator import pypi_investigator
from pypi_investigator import cli


class TestPypi_investigator(unittest.TestCase):
    """Tests for `pypi_investigator` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'pypi_investigator.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
