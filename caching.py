import hashlib
import pickle

# Create a cache dictionary to store responses (in-memory for simplicity)
response_cache = {}

def generate_cache_key(image, prompt):
    """Generates a unique key for the image and prompt combination."""
    image_hash = hashlib.md5(image.tobytes()).hexdigest()
    prompt_hash = hashlib.md5(prompt.encode()).hexdigest()
    return f"{image_hash}-{prompt_hash}"

def get_cached_response(image, prompt):
    """Retrieves the response from the cache if available."""
    cache_key = generate_cache_key(image, prompt)
    if cache_key in response_cache:
        return response_cache[cache_key]
    return None

def cache_response(image, prompt, response):
    """Stores the response in the cache."""
    cache_key = generate_cache_key(image, prompt)
    response_cache[cache_key] = response