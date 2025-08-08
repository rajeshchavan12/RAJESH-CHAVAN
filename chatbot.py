import re

class SimpleChatbot:
    def __init__(self):
        self.rules = {
            r'hello|hi|hey': 'Hello! How can I help you today?',
            r'how are you': 'I am just a bot, but I am doing great! How about you?',
            r'what is your name': 'I am InsureAI, your virtual insurance assistant.',
            r'what can you do': 'I can answer basic questions about our insurance products. What would you like to know?',
            r'insurance|plans|products': 'We offer a variety of insurance plans, including life, health, and auto insurance. Which one are you interested in?',
            r'life insurance': 'Life insurance provides a payment to your beneficiaries when you pass away. It is a great way to protect your family\'s financial future.',
            r'health insurance': 'Health insurance helps cover the cost of medical care. We have several plans with different levels of coverage.',
            r'auto insurance': 'Auto insurance protects you against financial loss if you have an accident. We offer competitive rates.',
            r'quote|price|cost': 'To get a personalized quote, please contact one of our human agents. I can provide you with their contact information.',
            r'contact|agent|human': 'You can reach our agents by phone at 1-800-555-1234 or by email at agents@insureai.com.',
            r'bye|goodbye': 'Goodbye! Have a great day!',
            r'.*': 'I am not sure how to answer that. Can you ask me something else? Or you can contact one of our agents for more complex questions.'
        }

    def get_response(self, message):
        message = message.lower()
        for pattern, response in self.rules.items():
            if re.search(pattern, message):
                return response
        return self.rules['.*'] # Default response
