from flask import Flask, render_template, request, jsonify
from models.generate_poem import generate_poem, generate_multiple_poems, explain_poem
from models.intelligent_prompts import suggest_prompt
from models.fine_tune import fine_tune_on_user_data
from models.multilingual import generate_poem_in_language

app = Flask(__name__)

@app.route("/")
def index():
    # Render the main page with a suggested prompt
    suggested_prompt = suggest_prompt()
    return render_template("index.html", suggested_prompt=suggested_prompt)

@app.route("/generate", methods=["POST"])
def generate():
    # Generate poems based on user input
    data = request.json
    prompt = data.get("prompt")
    theme = data.get("theme", "nature")
    style = data.get("style", "free verse")
    num_poems = int(data.get("num_poems", 1))
    language = data.get("language", "en")

    if language != "en":
        poems = [generate_poem_in_language(prompt, language)]
    else:
        poems = generate_multiple_poems(prompt, theme=theme, style=style, num_poems=num_poems)
    return jsonify(poems=poems)

@app.route("/explain", methods=["POST"])
def explain():
    # Explain how the AI generated the poem
    data = request.json
    poem = data.get("poem")
    explanation = explain_poem(poem)
    return jsonify(explanation=explanation)

@app.route("/upload", methods=["POST"])
def upload_poems():
    # Handle user poem uploads for fine-tuning
    uploaded_file = request.files["poem_file"]
    if uploaded_file:
        file_path = "data/user_poems.txt"
        uploaded_file.save(file_path)
        fine_tune_on_user_data(file_path)
        return jsonify({"message": "Model fine-tuned successfully!"})
    return jsonify({"error": "No file uploaded."}), 400

if __name__ == "__main__":
    app.run(debug=True)
