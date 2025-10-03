# test_ngrxeffects.py
"""
Tests for NgRxEffects module.
"""

import unittest
from ngrxeffects import NgRxEffects

class TestNgRxEffects(unittest.TestCase):
    """Test cases for NgRxEffects class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NgRxEffects()
        self.assertIsInstance(instance, NgRxEffects)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NgRxEffects()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
