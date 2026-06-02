# CodeAlpha Task 2: Chatbot for FAQs - NO NLTK VERSION
# Domain: Artificial Intelligence
# Student: Pushpanjali Kumari

import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def simple_tokenize(text):
    """NLTK ke bina simple tokenizer"""
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.split()

def preprocess_text(text):
    stop_words = {'is', 'the', 'a', 'an', 'and', 'or', 'to', 'of', 'in', 'for', 'on', 'with', 'how', 'what', 'i', 'me', 'will', 'do'}
    tokens = simple_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

def codealpha_faq_bot():
    print("="*60)
    print("Bot: Hello! I am CodeAlpha FAQ Bot")
    print("Bot: Ask me about CodeAlpha AI Internship. Type 'bye' to exit.")
    print("="*60)

    faq_database = {
        "what is codealpha": "CodeAlpha is a platform offering 1-month virtual internships in AI, Web Dev, Python, Java with real-world projects and verified certificates.",
        "how to apply for codealpha internship": "Step 1: Visit codealpha.tech. Step 2: Select Artificial Intelligence domain. Step 3: Fill the application form. Step 4: Wait for selection email.",
        "what is the duration of codealpha internship": "The CodeAlpha internship duration is 1 month. You must complete 2 or 3 tasks in your selected domain to get the certificate.",
        "will i receive certificate from codealpha": "Yes, you will get a verified completion certificate after successfully submitting all 2 or 3 tasks via the official Google Form.",
        "is codealpha internship paid or free": "CodeAlpha internships are unpaid virtual internships. They focus on skill development, project experience, and portfolio building.",
        "how many tasks in ai domain codealpha": "In AI domain you need to complete any 2 or 3 tasks from: Language Translator Tool, FAQ Chatbot, Music Generation with AI.",
        "where to submit codealpha tasks": "Submit your completed tasks through the official CodeAlpha Google Form link shared in your selection email.",
        "hi hello": "Hello! How can I help you with CodeAlpha AI Internship queries today?"
    }

    questions = list(faq_database.keys())
    answers = list(faq_database.values())
    processed_questions = [preprocess_text(q) for q in questions]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(processed_questions)

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == 'bye':
            print("Bot: Thank you! All the best for your CodeAlpha internship.")
            break

        if not user_input:
            continue

        processed_user_input = preprocess_text(user_input)
        user_tfidf = vectorizer.transform([processed_user_input])
        cosine_scores = cosine_similarity(user_tfidf, tfidf_matrix)
        best_index = np.argmax(cosine_scores)
        best_score = cosine_scores[0][best_index]

        if best_score > 0.2:
            print(f"Bot: {answers[best_index]}")
        else:
            print("Bot: Sorry, I don't understand. Ask about: codealpha, apply, duration, certificate, tasks")

if __name__ == "__main__":
    codealpha_faq_bot()