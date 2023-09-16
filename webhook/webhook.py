from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the JSON data from the incoming request
    data = request.get_json()

    # Process the data (you can customize this part for your specific use case)
    if data:
        print("Received webhook data:")
        print(data)
        # Perform actions based on the data received

    return jsonify({"message": "Webhook received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
