import os
import threading
from dotenv import load_dotenv
from google import genai
import tkinter as tk
from tkinter import ttk, scrolledtext

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
chat = client.chats.create(model="gemini-2.5-flash")

# --- Main Window ---
window = tk.Tk()
window.title("🤖 Gemini Chatbot")
window.geometry("600x500")
window.minsize(400, 300)

# --- Styling ---
window.configure(bg="#a31780")

style = ttk.Style()
style.configure("TFrame", background="#57045e")
style.configure("TButton", 
                background="#13010D", 
                foreground="black",
                padding=8,
                font=("Arial", 10))
style.configure("TEntry", padding=8)
 
# --- Chat History ---
chat_frame = ttk.Frame(window)
chat_frame.pack(fill="both", expand=True, padx=10,pady=(10,0))

chat_history = tk.scrolledtext.ScrolledText(
    chat_frame, 
    state="disabled", 
    wrap="word",
    bg="#1e1e2e",  
    fg="white",
    font=("Consolas", 11),
    relief="flat",
    padx=10,
    pady=10
)
chat_history.pack(fill="both", expand=True)

import threading

def send_message():
    user_input = message_entry.get()
    
    if not user_input:
        return
    
    message_entry.delete(0, tk.END)
    message_entry.configure(state="disabled")  # disable input while waiting
    
    # show user message
    chat_history.configure(state="normal")
    chat_history.insert(tk.END, "You: " + user_input + "\n")
    chat_history.configure(state="disabled")
    chat_history.see(tk.END)
    
    # show thinking indicator
    chat_history.configure(state="normal")
    chat_history.insert(tk.END, "Gemini: thinking...\n\n")
    chat_history.configure(state="disabled")
    chat_history.see(tk.END)
    
    def get_response():
        response = chat.send_message(user_input)
        window.after(0, lambda: show_response(response.text))
    
    threading.Thread(target=get_response, daemon=True).start()

def show_response(reply):
    # remove "thinking..." and replace with real reply
    chat_history.configure(state="normal")
    content = chat_history.get("1.0", tk.END)
    content = content.replace("Gemini: thinking...\n\n", "")
    chat_history.delete("1.0", tk.END)
    chat_history.insert(tk.END, content)
    chat_history.insert(tk.END, "Gemini: " + reply + "\n\n")
    chat_history.configure(state="disabled")
    chat_history.see(tk.END)
    message_entry.configure(state="normal")  # re-enable input
    message_entry.focus()                     # put cursor back in input box

# --- Input Area ---
input_frame = ttk.Frame(window)
input_frame.pack(fill="x", padx=10, pady=(5, 15))
message_entry = tk.Entry(
    input_frame, 
    font=("Arial", 11),
    bg="#EFF0F1",
    fg="black",
    insertbackground="black",  #corsor color
    relief="flat"
)
message_entry.pack(side="left", fill="x", expand=True, padx=(0, 8))
message_entry.bind("<Return>", lambda event: send_message())
send_button = ttk.Button(input_frame, text="Send", command=send_message)
send_button.pack(side="right")


# --- Welcome Message ---
chat_history.configure(state="normal")
chat_history.insert(tk.END, "Gemini: Hello! I'm your AI assistant. How can I help you today?\n\n")
chat_history.configure(state="disabled")

window.mainloop()

