from flask import Flask, request, render_template_string
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)

# HTML Interface with Improved UI
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Summarization</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            text-align: center;
            background: linear-gradient(to right, #2C3E50, #4CA1AF);
            color: black;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 60%;
            margin: auto;
            padding: 20px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            margin-top: 50px;
            box-shadow: 0px 0px 15px rgba(255, 255, 255, 0.2);
        }
        h1 {
            font-size: 28px;
            font-weight: 600;
        }
        textarea {
            width: 90%;
            height: 150px;
            padding: 10px;
            border-radius: 8px;
            border: none;
            font-size: 16px;
            margin-top: 10px;
            box-shadow: inset 0px 0px 5px rgba(0, 0, 0, 0.2);
        }
        .btn {
            background: #4CA1AF;
            border: none;
            color: white;
            padding: 12px 20px;
            font-size: 18px;
            cursor: pointer;
            border-radius: 5px;
            margin-top: 15px;
            transition: 0.3s;
        }
        .btn:hover {
            background: #2C3E50;
        }
        .summary-box {
            margin-top: 20px;
            padding: 15px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 8px;
            font-size: 16px;
            color: white;
            text-align: left;
        }
        footer {
            margin-top: 30px;
            padding: 10px;
            background: rgba(255, 255, 255, 0.2);
            color: white;
            text-align: center;
            font-size: 14px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Text Summarization</h1>
        <form method="POST">
            <textarea name="text" placeholder="Enter your text here...">{{ text }}</textarea><br>
            <button type="submit" class="btn">Summarize</button>
        </form>
        {% if summary %}
        <h2>Summary</h2>
        <div class="summary-box">{{ summary }}</div>
        {% endif %}
        <footer>
        Designed & Developed by <strong>J DINESH CHOWDARY</strong> <br>
        Contact: <a href="mailto:dineshwalker143@gmail.com" style="color: #f8c471;">dineshwalker143@gmail.com</a>
    </footer>
    </div>
</body>
</html>
"""

def summarize_text(text):
    """Summarizes the given text using frequency-based scoring."""
    doc = nlp(text)
    stopwords = nlp.Defaults.stop_words
    word_frequencies = {}

    for word in doc:
        if word.text.lower() not in stopwords and word.is_alpha:
            word_frequencies[word.text] = word_frequencies.get(word.text, 0) + 1

    max_freq = max(word_frequencies.values(), default=1)
    for word in word_frequencies:
        word_frequencies[word] /= max_freq

    sentence_scores = {}
    for sent in doc.sents:
        for word in sent:
            if word.text.lower() in word_frequencies:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word.text.lower()]

    sentences = list(doc.sents)  # Convert generator to list
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:max(1, len(sentences) // 3)]
    summary = " ".join([sent.text for sent in summary_sentences])
    
    return summary

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    text = ""

    if request.method == "POST":
        text = request.form["text"]
        if text.strip():
            summary = summarize_text(text)

    return render_template_string(HTML_TEMPLATE, text=text, summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
