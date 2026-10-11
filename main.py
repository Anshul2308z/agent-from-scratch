from dotenv import load_dotenv
import os
from openai import OpenAI
from call_function_schema import available_functions

import argparse 

def generate_content(client, messages):
            
    response = client.chat.completions.create(
    model = "openrouter/free",
    messages = messages,
    tools = available_functions 
    )
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
    from prompts import system_prompt
    messages = [
        {
            "role":"system",
            "content": system_prompt
        },
        {
            "role":"user",
            "content": prompt,
        }]
    
    response = generate_content(client, messages)

    if verbose ==True :
        usage = response.usage
        verbose_output(prompt, usage)

    message = response.choices[0].message

    import json
    from call_function import call_function
    
    for tool_call in message.tool_calls:
        function_args = json.loads(tool_call.function.arguments or "{}")
        result_message = call_function(tool_call, verbose= verbose)

        content = result_message["content"]

        if content is None: 
            raise Exception("The returned tool message should have a non-empty \"content\". ")

        if verbose:
            print(f"-> {result_message['content']}")
        
        
        


    print(response.choices[0].message.content)

    

if __name__ == "__main__":
    main()
    