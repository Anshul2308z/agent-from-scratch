from dotenv import load_dotenv
import os
from openai import OpenAI

import argparse 

def generate_content(client, messages):
            
    response = client.chat.completions.create(
    model = "openrouter/free",
    messages = messages )
    return response

def verbose_output(prompt, usage):

    print(f"User prompt: {prompt}")
    if usage: 
        print(f"Prompt tokens: {usage.prompt_tokens}")
        print(f"Response tokens: {usage.completion_tokens}")
    else: 
        raise RuntimeError("API req failed")




def main():
    load_dotenv()
    api_key = os.environ.get('OPENROUTER_API_KEY')
    if api_key is None:
        raise RuntimeError("OPENROUTER_API_KEY is not present in the runtime env")
    
    # argparse, I feel Natural writing it thanks to RAG course I did 
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("prompt", type=str, help="Prompt for our chatbot")

    #optional verbose flag
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    #args
    args = parser.parse_args()
    prompt = args.prompt 
    verbose = args.verbose

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    messages = [{
            "role":"user",
            "content": prompt,
        }]
    
    response = generate_content(client, messages)

    if verbose ==True :
        usage = response.usage
        verbose_output(prompt, usage)


    print(response.choices[0].message.content)

    

if __name__ == "__main__":
    main()
    