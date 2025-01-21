from text_preprocessing import preprocess_text
from gpt_integration import get_gpt_response

def generate_response(user_message):
    preprocessed_message = preprocess_text(user_message)
    response = get_gpt_response(preprocessed_message)
    return response
