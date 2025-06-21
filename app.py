from flask import Flask, render_template, request
import joblib
import re
import os
import nltk
from nltk.corpus import stopwords
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Load environment variables
load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

# Load models
model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")
label_encoder = joblib.load("model/label_encoder.pkl")

# Hugging Face Client
client = InferenceClient("meta-llama/Meta-Llama-3-8B-Instruct", token=HF_TOKEN)

app = Flask(__name__)

# Text cleaner
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

# AI resource generator
def generate_resources_llama(style):
    prompt = f"""
    You are an educational AI assistant. Suggest 3 high-quality, free online resources for a college student who is a {style} learner.
    Also include 1 personalized study habit tip. Use bullet points.
    """
    response = client.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    resources = None
    tip = None
    if request.method == 'POST':
        sentence = request.form.get('sentence')
        if sentence:
            cleaned = clean_text(sentence)
            vectorized = vectorizer.transform([cleaned])
            pred = model.predict(vectorized)
            style = label_encoder.inverse_transform(pred)[0]

            tips = {
                "Visual": "Use diagrams, color-coded notes, videos, and charts.",
                "Auditory": "Listen to podcasts, record lectures, and discuss with peers.",
                "Kinesthetic": "Use hands-on tasks, models, and simulations.",
                "Reading-Writing": "Read books and blogs and write summaries."
            }
            prediction = style
            tip = tips.get(style)
            resources = generate_resources_llama(style)
    
    return render_template('index.html', prediction=prediction, tip=tip, resources=resources)

if __name__ == '__main__':
    app.run(debug=True)