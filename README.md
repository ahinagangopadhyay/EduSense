# 🎓 EduSense: AI-Powered Personalized Learning Style Assistant

Welcome to **EduSense** – an intelligent web app that predicts your learning style based on how you describe your study habits and then offers **AI-curated resources** tailored to your preferences.

---

## 🚀 What is EduSense?

**EduSense** combines the power of **Machine Learning** and **Generative AI** to help learners understand **how they learn best** — Visual, Auditory, Kinesthetic, or Reading-Writing.

✅ The app uses a **trained and tested ML model** to classify the user’s learning style  
🤖 Then it calls **LLaMA-3 (via Hugging Face)** to generate personalized study tips and online resources

---

## 🤖 ML Model Overview

The learning style prediction is powered by a trained **Logistic Regression model** (or optionally **LSTM/BERT**), which has been:

- ✅ Preprocessed using NLTK and TF-IDF vectorization
- ✅ Trained on a balanced dataset of 15,000+ labeled sentences
- ✅ Tested with high accuracy on a validation set


## ✨ Features

- 🔍 **Learning Style Predictor** trained on 3k+ labeled descriptions( custom created for the task)
- 🧠 **AI Recommendations** powered by LLaMA-3 (via Hugging Face Inference API)
- ✅ Tested on a separate test set to ensure accurate classification
- 🛠️ Built with **Flask**, **scikit-learn**, and **joblib**
- 🎨 Responsive, clean frontend with HTML/CSS
- 🔐 Secret token protection using `.env`

---

## 🧩 Learning Styles Covered

| Style            | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| **Visual**       | Learn best through images, diagrams, colors, and spatial understanding      |
| **Auditory**     | Prefer spoken information, podcasts, discussions, or lectures               |
| **Kinesthetic**  | Grasp concepts by doing – hands-on activities, simulations, real examples   |
| **Reading-Writing** | Excel when reading/writing notes, summaries, and text-heavy content       |

---

---

## 📸 Demo Preview
![image](https://github.com/user-attachments/assets/39d13707-ecf5-4630-be57-ec5ba86bfa67)


---

## 💻 Local Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/ahinagangopadhyay/EduSense.git
cd EduSense

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # or source venv/bin/activate on Linux/Mac

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up your .env file
echo HUGGINGFACE_TOKEN=your_token_here > .env

# 5. Run the Flask app
python app.py
