 from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    query = data.get("query", "No query provided")
    return jsonify({"response": f"Answering: {query}"})

if __name__ == '__main__':
    print("🚀 Flask server is starting...")
    app.run(debug=True)

