# test_postgreskit.py
"""
Tests for PostgresKit module.
"""

import unittest
from postgreskit import PostgresKit

class TestPostgresKit(unittest.TestCase):
    """Test cases for PostgresKit class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PostgresKit()
        self.assertIsInstance(instance, PostgresKit)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PostgresKit()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
