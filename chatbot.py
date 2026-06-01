# CodeAlpha Task 2: FAQ Chatbot
# Domain: Artificial Intelligence
# Student: Pushpanjali Kumari

def chatbot():
    print("Bot: Hello! I am CodeAlpha FAQ Bot. Type 'bye' to exit.")
    print("Bot: You can ask me about: hi, codealpha, apply, duration, certificate, stipend, tasks, help")
    
    faqs = {
        "hi": "Hello! How can I help you today?",
        "hello": "Hi there! Ask me anything about CodeAlpha.",
        "what is codealpha": "CodeAlpha is a platform offering virtual internships in tech domains like AI, Web Dev, etc.",
        "codealpha": "CodeAlpha provides 1-month virtual internships with real projects and certificates.",
        "how to apply": "Visit codealpha.tech and fill the internship application form for your domain.",
        "apply": "Go to codealpha.tech → Select your domain → Fill the form → Wait for selection mail.",
        "duration": "The internship duration is 1 month with 3 tasks to complete.",
        "certificate": "Yes, you will get a completion certificate after submitting all 3 tasks.",
        "stipend": "This is an unpaid virtual internship focused on learning and experience.",
        "tasks": "You need to complete 3 tasks in your chosen domain and submit them via the Google form.",
        "help": "You can ask me about: codealpha, apply, duration, certificate, stipend, tasks"
    }
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input == 'bye':
            print("Bot: Goodbye! All the best for your internship.")
            break
            
        elif user_input in faqs:
            print(f"Bot: {faqs[user_input]}")
            
        else:
            print("Bot: Sorry, I don't understand that. Type 'help' to see what I can answer.")

if __name__ == "__main__":
    chatbot()