from openai import OpenAI
import os
from dotenv import load_dotenv
from config import api_model, api_temperature, api_max_tokens, api_url

load_dotenv(dotenv_path="CONFIG.ENV")

def main():
    # Load API key from environment variable
    api_key = os.getenv("API_KEY")
    
    if not api_key:
        print("API key not found. Please set the API_KEY environment variable.")
        return
    
    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)
    
    # Example API call (replace with actual parameters as needed)
    response = client.chat.completions.create(
        model=api_model,
        messages=[{"role": "user", "content": "Exiba uma resposta de exemplo usando o modelo configurado."}],
        temperature=api_temperature,
        max_tokens=api_max_tokens
    )
    
    print(response.choices[0].message.content)

if __name__ == "__main__":    main()    