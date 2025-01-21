import unittest
from chatbot_logic import generate_response

class TestChatbot(unittest.TestCase):
    def test_generate_response(self):
        response = generate_response("Hello")
        self.assertIsInstance(response, str)

if __name__ == "__main__":
    unittest.main()
