from flask import Flask, render_template, request, jsonify
from chatbot import SimpleChatbot

app = Flask(__name__)
chatbot = SimpleChatbot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    message = request.json.get('message')
    response = chatbot.get_response(message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
