from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

def chat_with_bot(user_message):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful chatbot for an interior design business."},
            {"role": "user", "content": user_message}
        ]
    )
    return response["choices"][0]["message"]["content"]

@app.route("/chat", methods=["POST"])
def chatbot():
    data = request.json
    user_message = data.get("message")
    bot_reply = chat_with_bot(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
