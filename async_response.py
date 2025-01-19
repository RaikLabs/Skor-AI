import google.generativeai as genai
import asyncio
import time

async def generate_response(model, image, prompt):
    """Asynchronously generates a response from the model."""
    start_time = time.time()
    response = model.generate_content(
        [image, prompt],
        generation_config = genai.GenerationConfig(
        max_output_tokens=1000,
        temperature=0.1,
        )
    )  # Assuming an async method exists
    response_time = time.time() - start_time
    print(f"Response generated in {response_time:.2f} seconds")
    print(response.text)
    return response.text