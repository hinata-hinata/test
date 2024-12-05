import unittest
from unittest.mock import patch
from source.player import player_pon


class TestPlayerPon(unittest.TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_player_pon_g(self, mock_input):
        result = player_pon()
        self.assertEqual(result, "グー", "Test failed: Input '1' should return 'グー'")

    @patch('builtins.input', side_effect=['2'])
    def test_player_pon_c(self, mock_input):
        result = player_pon()
        self.assertEqual(result, "チョキ", "Test failed: Input '2' should return 'チョキ'")

    @patch('builtins.input', side_effect=['3'])
    def test_player_pon_p(self, mock_input):
        result = player_pon()
        self.assertEqual(result, "パー", "Test failed: Input '3' should return 'パー'")

    @patch('builtins.input', side_effect=['4', '1'])
    def test_player_pon_invalid_then_g(self, mock_input):
        # Invalid input first, then a valid input
        result = player_pon()
        self.assertEqual(result, "グー", "Test failed: After invalid input '4', input '1' should return 'グー'")

if __name__ == '__main__':
    unittest.main()