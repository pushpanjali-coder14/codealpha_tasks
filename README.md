# CodeAlpha AI Internship Tasks

This repository contains all 3 tasks completed for CodeAlpha AI Internship.

---

## ✅ TASK 1: Language Translation Tool

### Objective
Create a user interface where user can enter text and select source & target languages. Use a translation API and display the translated text clearly on screen.

### Key Features Implemented
- **User Interface**: Built a simple UI where users can enter text and select source & target languages
- **Translation API**: Used HuggingFace Transformers API with `Helsinki-NLP/opus-mt-en-hi` model
- **Processing**: Sends input text to the API and gets translated response
- **Display**: Shows translated text clearly on the screen
- **Bonus**: Added copy button for better usability

### Tech Stack
Python, HuggingFace Transformers, Gradio

### How to Run
```bash
cd Task1_LanguageTranslation
pip install transformers gradio
python app.py

---

## ✅ TASK 2: Chatbot for FAQs

### Objective
Build a chatbot that answers user queries by matching them with the most similar FAQ using NLP techniques.

### Key Features Implemented
- **FAQ Collection**: Collected FAQs related to a topic with questions and their answers
- **Text Preprocessing**: Used NLTK library to tokenize and clean the text data
- **Question Matching**: Implemented TF-IDF Vectorizer + Cosine Similarity to match user questions with FAQs
- **Chatbot Response**: Displays the best matching answer as chatbot response
- **Chat UI**: Created simple chat interface for user interaction

### Tech Stack
Python, NLTK, Scikit-learn, Pandas, Streamlit

### How to Run
```bash
cd Task2_ChatbotFAQs
pip install -r Requirements.txt
python chatbot.py

---

## ✅ TASK 3: Music Generation with AI

### Objective
Generate new music using AI by training a deep learning model on MIDI music data.

### Key Features Implemented
- **Data Collection**: Collected MIDI music data of J.S. Bach classical compositions
- **Preprocessing**: Converted MIDI files into note sequences suitable for training using `music21` library
- **Deep Learning Model**: Built RNN-based LSTM model to learn music patterns
- **Model Training**: Trained the model on dataset to generate new music sequences
- **Output Generation**: Converted generated sequences to MIDI and saved as audio file

### Tech Stack
Python, TensorFlow/Keras, Music21, NumPy

### How to Run
1. Install dependencies: `pip install -r Requirements.txt`
2. Train model: `python music_Generator.py`
3. Generate music: `python generate.py`

### Note
Trained model `music_model.h5` excluded from repository due to GitHub file size limits. Please retrain locally.

---

## 👩‍💻 Submitted by
**Name:** Pushpanjali  
**Organization:** CodeAlpha  
**Domain:** AI Internship  
**GitHub:** [@pushpanjali-coder14](https://github.com/pushpanjali-coder14)

---
**All 3 AI tasks completed and tested successfully ✅**
