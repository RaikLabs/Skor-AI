import asyncio
import google.generativeai as genai
import logging
import gc
from utils_gpu import configure_gpu
#import time
from response_time import calculate_response_time
from caching import get_cached_response, cache_response
from async_response import generate_response
from config import API_KEY
import PIL.Image
import matplotlib.pyplot as plt
from models import MODEL_FLASH, MODEL_FLASH_B, MODEL_FLASH_EXP, MODEL_PRO

sample_image_file = PIL.Image.open('cs2.png')

# Resize the image to 50% of its original size
resized_image = sample_image_file.resize((int(sample_image_file.width * 0.5), int(sample_image_file.height * 0.5)))

prompt = "Based on this frame, what should be my strategy and what plan should we execute in order to win the game. Keep it brief."

logging.basicConfig(level=logging.WARNING)

async def main():
    try:
        # configure_gpu()  # Call the GPU configuration function
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel(MODEL_FLASH)

        # Create an asynchronous task for the response generation
        response_task = asyncio.create_task(generate_response(model, sample_image_file, prompt))

        # Display the image (this will happen concurrently with response generation)
        plt.imshow(sample_image_file)
        plt.title("Input Image")
        plt.show()
        
        # Wait for the response task to complete
        response_text = await response_task

        # Cache the response
        cache_response(sample_image_file, prompt, response_text)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        try:
            del model
            gc.collect()
        except Exception as e:
            logging.warning(f"Error during cleanup: {e}")

if __name__ == "__main__":
    asyncio.run(main())