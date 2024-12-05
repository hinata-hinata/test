import unittest
from source.computer import computer_pon


class TestComputerPon(unittest.TestCase):
    def test_computer_pon(self):
        # 何度か関数を実行して、結果が期待される範囲内であることを確認します。
        possible_hands = ["グー", "チョキ", "パー"]

        for _ in range(100): 
            result = computer_pon()
            self.assertIn(result, possible_hands, f"Unexpected result: {result}")

if __name__ == '__main__':
  unittest.main()