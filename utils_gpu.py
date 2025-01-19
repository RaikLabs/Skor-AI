import google.generativeai as genai

def configure_gpu():
    """Configures the google.generativeai library to use GPU if available."""
    if genai.is_gpu_available():
        print("GPU is available. Configuring google.generativeai to use GPU.")
        genai.set_gpu_mode(True)  # Or any appropriate method to enable GPU usage
    else:
        print("GPU is not available. Using CPU.")