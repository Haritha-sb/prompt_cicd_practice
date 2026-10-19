
import unittest
from prompt import PROMPT


class TestPrompt(unittest.TestCase):
    def test_prompt_has_required_instructions(self):
        self.assertIn("water-resource analyst", PROMPT)
        self.assertIn("simple English", PROMPT)
        self.assertIn("three bullet points", PROMPT)
        self.assertIn("Do not invent rainfall values", PROMPT)


if __name__ == "__main__":
    unittest.main()
