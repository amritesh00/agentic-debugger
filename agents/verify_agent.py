from groq import Groq

client = Groq()

def verify_solution(code):

    prompt=f"""
    Check if this code logically fixes the bug.

    Code:
    {code}

    Respond with:
    VERIFIED or POSSIBLE ISSUE
    """

    response=client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content