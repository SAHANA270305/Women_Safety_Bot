import tkinter as tk
from tkinter import scrolledtext, simpledialog
import datetime
import os

# Global user name
user_name = "Anonymous"
log_file = "chatlog_Anonymous.txt"

# Create chat log directory if it doesn't exist
if not os.path.exists("chatlogs"):
    os.makedirs("chatlogs")

# Get chatbot response
def get_response(user_input):
    user_input = user_input.lower()
    if "emergency" in user_input or "help" in user_input:
        return "🚨 Please call 1091 (Women Helpline) or 112 (Emergency Services) immediately."
    elif "rights" in user_input:
        return "📜 You have the right to safety, dignity, and protection under Indian law. Key rights include FIR registration, free legal aid, and shelter."
    elif "violence" in user_input or "abuse" in user_input:
        return "⚠️ You're protected under the Domestic Violence Act, 2005. Please reach out to the police or NGOs for help."
    elif "law" in user_input:
        return "📚 Important laws include IPC Section 498A, Dowry Prohibition Act, and the POSH Act for workplace harassment."
    elif "ngo" in user_input or "support" in user_input:
        return "🤝 NGOs like Breakthrough, Sakshi, and SEWA Bharat can support you with legal and emotional help."
    else:
        return "🤖 I'm here to help with women’s rights and safety. Please ask me about legal help, emergency numbers, or support services."

# Log chat to file
def log_chat(speaker, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(os.path.join("chatlogs", log_file), "a", encoding="utf-8") as file:

        file.write(f"[{timestamp}] {speaker}: {message}\n")

# Handle sending message
def send_message():
    user_msg = user_input.get()
    if user_msg.strip() == "":
        return

    chat_area.insert(tk.END, f"{user_name}: {user_msg}\n")
    log_chat(user_name, user_msg)

    bot_response = get_response(user_msg)
    chat_area.insert(tk.END, f"Bot: {bot_response}\n\n")
    log_chat("Bot", bot_response)

    user_input.delete(0, tk.END)

# Ask user for name (login)
def get_user_profile():
    global user_name, log_file
    answer = simpledialog.askstring("User Login", "Enter your name (or leave blank to remain anonymous):")
    if answer and answer.strip():
        user_name = answer.strip()
    else:
        user_name = "Anonymous"
    log_file = f"chatlog_{user_name}.txt"

# GUI setup
def start_chatbot():
    get_user_profile()

    window = tk.Tk()
    window.title("Women's Safety & Rights Chatbot")
    window.geometry("520x500")

    title = tk.Label(window, text="🛡️ Women's Safety & Rights Chatbot", font=("Arial", 14, "bold"))
    title.pack(pady=10)

    global chat_area
    chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, font=("Arial", 10))
    chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    global user_input
    user_input = tk.Entry(window, font=("Arial", 10))
    user_input.pack(padx=10, pady=5, fill=tk.X)

    send_btn = tk.Button(window, text="Send", command=send_message)
    send_btn.pack(pady=5)

    welcome_msg = f"🤖 Welcome {user_name}! You can ask me about your rights, laws, safety, or support.\n\n"
    chat_area.insert(tk.END, welcome_msg)
    log_chat("Bot", welcome_msg.strip())

    window.mainloop()

# Run the chatbot
start_chatbot()
