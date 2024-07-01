from flask import Flask, request, jsonify

app = Flask(__name__)

responses = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm just a program, but I'm functioning as expected. How about you?",
    "what is your name": "I am an AI chatbot created by OpenAI.",
    "what can you do": "I can chat with you and help answer your questions!",
    "bye": "Goodbye! Have a great day!"
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return "I'm sorry, I don't understand that."

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data['message']
    response = get_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run()
