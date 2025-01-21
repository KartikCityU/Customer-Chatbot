import openai

# Set your OpenAI API key
openai.api_key = 'your_openai_api_key'

def get_gpt_response(user_message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_message}],
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"An error occurred: {e}"
