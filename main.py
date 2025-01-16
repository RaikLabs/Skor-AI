import google.generativeai as genai
from models import MODEL_FLASH_EXP, MODEL_FLASH, MODEL_FLASH_B, MODEL_PRO
from config import API_KEY
import logging
import gc
import PIL.Image
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import scrolledtext

sample_image_file = PIL.Image.open('cs2.png')

prompt = "Based on this frame, what should be my strategy and what plan should we execute in orde to win the game"

# Configure logging to capture warnings and errors
logging.basicConfig(level=logging.WARNING)

def display_response(response_text):
    """Displays the AI's response in a new Tkinter window."""
    window = tk.Tk()
    window.title("AI Response")
    text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD)
    text_area.insert(tk.INSERT, response_text)
    text_area.pack(expand=True, fill='both')
    window.mainloop()

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(MODEL_FLASH_EXP)
    response = model.generate_content([sample_image_file, prompt])
    print(response)
    #plt.imshow(response)
    plt.imshow(sample_image_file)
    plt.title("Input Image")
    plt.show()

        # Display the response in a separate window
    if response.text:
        display_response(response.text) 
    else:
        print("No response generated.")

except Exception as e:
    logging.error(f"An error occurred: {e}") 
finally:
    try:
        # explicitly delete the model
        del model
        gc.collect()
    except Exception as e:
        logging.warning(f"Error during cleanup: {e}")
