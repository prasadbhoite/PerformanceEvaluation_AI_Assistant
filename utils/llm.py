from openai import OpenAI

def generate_completion(prompt, model="gpt-4o", temperature=0.7, api_key=None):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    return response.choices[0].message.content.strip()
