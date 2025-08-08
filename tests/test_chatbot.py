import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chatbot import SimpleChatbot

class TestSimpleChatbot(unittest.TestCase):

    def setUp(self):
        self.chatbot = SimpleChatbot()

    def test_greeting(self):
        self.assertEqual(self.chatbot.get_response("hello"), "Hello! How can I help you today?")
        self.assertEqual(self.chatbot.get_response("hi"), "Hello! How can I help you today?")
        self.assertEqual(self.chatbot.get_response("hey"), "Hello! How can I help you today?")

    def test_name(self):
        self.assertEqual(self.chatbot.get_response("what is your name"), "I am InsureAI, your virtual insurance assistant.")

    def test_insurance_plans(self):
        self.assertIn("life, health, and auto insurance", self.chatbot.get_response("tell me about your plans"))

    def test_contact(self):
        self.assertIn("1-800-555-1234", self.chatbot.get_response("how can I contact an agent?"))

    def test_unknown_question(self):
        self.assertIn("I am not sure how to answer that", self.chatbot.get_response("what is the meaning of life?"))

if __name__ == '__main__':
    unittest.main()
