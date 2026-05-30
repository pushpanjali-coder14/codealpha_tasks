import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

def translate_text():
    try:
        text = input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter text to translate")
            return
        
        src = source_lang.get()
        dest = target_lang.get()
        
        translator = Translator()
        result = translator.translate(text, src=src, dest=dest)
        
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result.text)
        
    except Exception as e:
        messagebox.showerror("Error", "Translation failed. Check your internet connection.")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", tk.END).strip())
    messagebox.showinfo("Success", "Translation copied to clipboard!")

def clear_all():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

# Main Window
root = tk.Tk()
root.title("CodeAlpha - Language Translation Tool")
root.geometry("750x600")
root.configure(bg="#f5f5f5")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Language Translation Tool", font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#333")
title_label.pack(pady=15)

tk.Label(root, text="Task 1 - CodeAlpha Artificial Intelligence Internship", font=("Arial", 10), bg="#f5f5f5", fg="#666").pack()

# Language Selection Frame
lang_frame = tk.Frame(root, bg="#f5f5f5")
lang_frame.pack(pady=15)

tk.Label(lang_frame, text="From:", bg="#f5f5f5", font=("Arial", 11, "bold")).grid(row=0, column=0, padx=10)
source_lang = ttk.Combobox(lang_frame, values=list(LANGUAGES.keys()), width=25, state="readonly", font=("Arial", 10))
source_lang.set('en')
source_lang.grid(row=0, column=1, padx=10)

tk.Label(lang_frame, text="To:", bg="#f5f5f5", font=("Arial", 11, "bold")).grid(row=0, column=2, padx=10)
target_lang = ttk.Combobox(lang_frame, values=list(LANGUAGES.keys()), width=25, state="readonly", font=("Arial", 10))
target_lang.set('hi')
target_lang.grid(row=0, column=3, padx=10)

# Input Text
tk.Label(root, text="Enter Text:", bg="#f5f5f5", font=("Arial", 11, "bold")).pack(anchor="w", padx=40, pady=(10,0))
input_text = tk.Text(root, height=8, width=80, font=("Arial", 11), wrap=tk.WORD, relief=tk.SOLID, borderwidth=1)
input_text.pack(pady=5)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#f5f5f5")
btn_frame.pack(pady=15)

translate_btn = tk.Button(btn_frame, text="Translate", command=translate_text, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), width=15, height=1, cursor="hand2", relief=tk.RAISED, borderwidth=2)
translate_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(btn_frame, text="Clear All", command=clear_all, bg="#f44336", fg="white", font=("Arial", 12, "bold"), width=15, height=1, cursor="hand2", relief=tk.RAISED, borderwidth=2)
clear_btn.grid(row=0, column=1, padx=10)

# Output Text
tk.Label(root, text="Translated Text:", bg="#f5f5f5", font=("Arial", 11, "bold")).pack(anchor="w", padx=40, pady=(5,0))
output_text = tk.Text(root, height=8, width=80, font=("Arial", 11), wrap=tk.WORD, relief=tk.SOLID, borderwidth=1)
output_text.pack(pady=5)

# Copy Button
copy_btn = tk.Button(root, text="Copy Translation", command=copy_to_clipboard, bg="#2196F3", fg="white", font=("Arial", 11, "bold"), width=20, cursor="hand2", relief=tk.RAISED, borderwidth=2)
copy_btn.pack(pady=10)

# Footer
tk.Label(root, text="Developed by Pushpanjali Kumari | CodeAlpha Internship", bg="#f5f5f5", fg="#888", font=("Arial", 9)).pack(side=tk.BOTTOM, pady=10)

root.mainloop()