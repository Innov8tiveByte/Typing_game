import tkinter as tk
import random
import time

# List of sample words for typing test
word_list = ['apple', 'banana', 'cherry', 'dog', 'elephant', 'flower', 'grape', 'hamburger', 'igloo', 'jacket']

def start_typing_test():
    input_text.delete('1.0', tk.END)  # Clear previous text
    random_word = random.choice(word_list)
    display_text.config(text=random_word)
    start_time = time.time()
    input_text.bind('<KeyRelease>', lambda event: check_typing(event, random_word, start_time))

def check_typing(event, random_word, start_time):
    typed_text = input_text.get('1.0', tk.END).strip()
    if typed_text == random_word:
        end_time = time.time()
        time_taken = end_time - start_time
        wpm = calculate_wpm(time_taken, len(random_word))
        result_label.config(text=f"Your WPM: {wpm:.2f}")
        input_text.unbind('<KeyRelease>')  # Disable typing after completion

def calculate_wpm(time_taken, word_length):
    seconds_per_minute = 60
    characters_per_word = 5  # Average word length
    wpm = (characters_per_word / time_taken) * seconds_per_minute
    return wpm

# Create the main window
root = tk.Tk()
root.title("Typing Test")

# Create and place widgets
display_text = tk.Label(root, text="", font=("Helvetica", 24))
display_text.pack(pady=20)

input_text = tk.Text(root, height=1, font=("Helvetica", 18))
input_text.pack()

start_button = tk.Button(root, text="Start Typing Test", command=start_typing_test)
start_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
