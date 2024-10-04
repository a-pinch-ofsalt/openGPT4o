from flask import Flask, request, jsonify
from gradio_client import Client
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_gpt_result(prompt):
    print(f"Prompt: {prompt}")
    client = Client("KingNish/OpenGPT-4o")
    result = client.predict(
		user_prompt={"text":"","files":[]},
		api_name="/chat"
)
    print(f"result: {result}")
    return result

# Route to accept HTML POST requests
@app.route('/message', methods=['POST'])
def post_data():
    # Extract data from the incoming HTML POST request
    if request.method == 'POST':
        data = request.form['input']
        result = get_gpt_result(data)
        return jsonify({"result": result})
    else:
        return jsonify({"error": "Invalid request method"}), 400

# You no longer need to run Flask in a separate thread.
# Instead, you will configure gunicorn to handle the Flask app.
if __name__ == "__main__":
    # Launch the Gradio app without `share=True` in production
    app.launch(server_name="0.0.0.0", server_port=7860)
