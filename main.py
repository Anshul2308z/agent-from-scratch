from dotenv import load_dotenv
import os

from openai import OpenAI

def main():
    load_dotenv()
    api_key = os.environ.get('OPENROUTER_API_KEY')
    if api_key is None:
        raise RuntimeError("OPENROUTER_API_KEY is not present in the runtime env")
    print("Hello from bootdev-agent!")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )
    response = client.chat.completions.create(
        model = "openrouter/free",
        messages = [{
            "role":"user",
            "content": "What is Raskolnikov's theory in crime and punishment, revolving around extraordinary, intelligent people. Give a concise answer, about 4-5 lines"
        }]
    )

    print(response.choices[0].message.content)

    

if __name__ == "__main__":
    main()
