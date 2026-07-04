# 🤖 Gemini AI Chatbot

A desktop AI chatbot built with Python and Google's Gemini API.
Supports real conversations with memory using the Gemini 2.5 Flash model.

## ✅ Features

* ✅ Connects to real Gemini AI
* ✅ Remembers conversation history
* ✅ Has a GUI with dark theme
* ✅ Threading so window doesn't freeze
* ✅ Shows "thinking..." while waiting
* ✅ Press Enter to send messages

## 🚀 How to Run


1. Clone the repository
   git clone https://github.com/kinza-ai-tech/gemini-chatbot

2. Install dependencies
   pip install google-genai python-dotenv

3. Create a .env file and add your API key
   GEMINI_API_KEY=your_key_here

4. Run the chatbot
   python gui.py

## 📁 Project Structure

gemini-ai-chatbot/
│
├── chat.py         
├── gui.py          
├── .env             
├── .gitignore
└── README.md

## 🧠 What I Learned

* ✅ Gemini API: Used google-genai SDK to connect Python to real AI model
* ✅ Threading: Ran API calls in background so GUI never freezes while waiting
* ✅ dotenv: Stored API key safely in .env file instead of hardcoding in code
* ✅ Tkinter: Built styled dark theme chat window with ScrolledText and ttk widgets