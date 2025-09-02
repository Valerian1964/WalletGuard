# test_walletguard.py
"""
Tests for WalletGuard module.
"""

import unittest
from walletguard import WalletGuard

class TestWalletGuard(unittest.TestCase):
    """Test cases for WalletGuard class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WalletGuard()
        self.assertIsInstance(instance, WalletGuard)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WalletGuard()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
