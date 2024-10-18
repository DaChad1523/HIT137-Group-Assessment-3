from groq import Groq
import tkinter as tk

client = Groq(api_key="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")

def open_ai(user_input):
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=1,
        max_tokens=650,
        top_p=1,
        stream=True,
        stop=None,
    )

    ai_response.config(state=tk.NORMAL)  
    for chunk in completion:
        content = chunk.choices[0].delta.content or ""
        print(content, end="")
        ai_response.insert(tk.END, content)
        ai_response.see(tk.END)

    ai_response.config(state=tk.DISABLED)

def on_button_click():
    ai_response.config(state=tk.NORMAL)
    ai_response.delete("1.0", tk.END) 
    open_ai(text_box.get("1.0", tk.END).strip())
    ai_response.config(state=tk.DISABLED)
    ai_response.see("1.0")

root = tk.Tk()
root.title("Chatbot")
root.geometry("600x600") 

label = tk.Label(root, text="User Input:")
label.pack(pady=10)

text_box = tk.Text(root, height=5, width=60, wrap=tk.WORD)
text_box.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

submit_button = tk.Button(button_frame, text="Submit", command=on_button_click)
submit_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(button_frame, text="Clear", command=lambda: text_box.delete("1.0", tk.END))
delete_button.pack(side=tk.LEFT, padx=5)

ai_response = tk.Text(root, height=20, width=60, wrap=tk.WORD)
ai_response.pack(pady=10)
ai_response.config(state=tk.DISABLED) 

root.mainloop()
