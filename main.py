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

    import json
    from call_function import call_function

    for _ in range(20):
        response = generate_content(client, messages)

        if verbose ==True :
            usage = response.usage
            verbose_output(prompt, usage)

        message = response.choices[0].message

        #Agent is not calling any tools! 
        if not message.tool_calls:
            print( message.content )
            return 
        messages.append(
            message
        )

        #Agent has tool_calls to make! 
        for tool_call in message.tool_calls:

            result_message = call_function(tool_call, verbose= verbose)

            content = result_message["content"]

            if content is None: 
                raise Exception("The returned tool message should have a non-empty \"content\". ")

            if verbose:
                print(f"-> {result_message['content']}")

            messages.append(
                result_message
            )
    else:
        #this is the so called for else structure, so I replaced my checking of _ == 19 by this, as 20 is the limit of iterations we have allowed, _ spans from 0 to 19.
        exit(code=1)


        

    

if __name__ == "__main__":
    main()
    