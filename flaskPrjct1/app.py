from flask import Flask, render_template, request, jsonify
import json, random, pickle

app = Flask(__name__)

model = pickle.load(open('intent_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

with open('intents.json') as f:
    intents = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json['message']
    X = vectorizer.transform([message.lower()])
    tag = model.predict(X)[0]

    for intent in intents['intents']:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return jsonify({'response': response})
    
    return jsonify({'response': "Maaf, saya tidak mengerti."})

if __name__ == '__main__':
    app.run(debug=True)
