from groq import Groq

client = Groq()

def detect_error(code,error):

    prompt=f"""
    You are a programming debugging expert.

    Code:
    {code}

    Error:
    {error}

    Explain:
    1. Error type
    2. Cause
    """

    response=client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content