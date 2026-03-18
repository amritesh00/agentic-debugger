from groq import Groq

client = Groq()

def generate_fix(code,error,docs):

    prompt=f"""
    Fix the code based on the error.

    Code:
    {code}

    Error:
    {error}

    Reference:
    {docs}

    Provide corrected code only.
    """

    response=client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content