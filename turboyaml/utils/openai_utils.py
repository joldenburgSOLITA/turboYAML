import openai
import os

def get_client(api_key):
    try:
        api_key = api_key or os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("API key is missing. Provide it via --api-key or the OPENAI_API_KEY environment variable.")

        # Correct OpenAI client initialization for v1.x
        client = openai.OpenAI(api_key=api_key)
        
        # Test API connection
        client.models.list()
        
        return client
    except Exception as e:
        raise ValueError(f"Failed to initialize OpenAI client: {e}")


async def send_to_openai(messages, api_key, model):
    # Set up OpenAI API credentials
    client = AsyncOpenAI(api_key=api_key)

    # Send the prompt to the OpenAI API to retrieve the YAML output
    response = await client.chat.completions.create(
        model=model, messages=messages, temperature=0.6
    )
    return response
