"""
RoastMyPM — backend (the "brain").

Step 4: tool + DB. The LLM can now call get_strong_examples(dimension)
to fetch curated bullet examples from SQLite instead of guessing.
"""

import os
import json
from groq import Groq
from dotenv import load_dotenv
from database import init_db, get_strong_examples

load_dotenv()
init_db()  # Creates DB + seeds it on first run; no-op after that

SYSTEM_PROMPT = """You are a brutally honest PM hiring manager with 15 years of experience at top product companies like Razorpay, Swiggy, and CRED.

Your job: roast résumé bullets so PMs are forced to write with real impact. Not to be cruel — to be useful.

Rules:
- Call out vague language ("managed", "worked on", "collaborated", "helped") — demand specifics.
- Flag missing metrics ruthlessly. "Improved onboarding" is meaningless. "Reduced onboarding drop-off by 34%" is a bullet.
- Always call get_strong_examples() for the most relevant dimension before writing your roast — ground your advice in real curated data, not just training knowledge.
- If the bullet is actually strong, say so — but always suggest how to push it further.
- Be direct, a little sarcastic, but constructive. You want this PM to get the job.
- Always end with a rewritten version that would impress a hiring manager.
- Remember the full conversation — if the user says "roast it harder" or "tailor for fintech", you know exactly what they mean.

Format your response exactly like this:
🔥 THE ROAST
[Your critique — 2–4 sentences]

✏️ REWRITTEN
[The improved bullet]

💡 WHY THIS WORKS
[One sentence on what makes the rewrite stronger]"""

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_strong_examples",
            "description": "Fetch curated strong and weak PM résumé bullet examples for a specific dimension from the database. Always use this to ground your critique in real examples.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dimension": {
                        "type": "string",
                        "enum": ["metrics", "action", "scope", "ownership", "outcome"],
                        "description": "metrics = numbers/impact, action = verbs used, scope = team/budget size, ownership = accountability level, outcome = results vs activities",
                    }
                },
                "required": ["dimension"],
            },
        },
    }
]


def get_response(messages: list) -> str:
    if not messages:
        return "Paste something first — I can't roast thin air."

    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        return (
            "⚠️ No GROQ_API_KEY found.\n\n"
            "**Local:** Add `GROQ_API_KEY=gsk_...` to your `.env` file.\n"
            "**Deployed:** Add it in Streamlit Cloud → App Settings → Secrets."
        )

    client = Groq(api_key=api_key)
    groq_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + messages

    # First call — LLM decides whether to call a tool
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=groq_messages,
        tools=TOOLS,
        tool_choice="auto",
        temperature=0.7,
        max_tokens=1024,
    )

    message = response.choices[0].message

    # If LLM called a tool, run it and send result back for the final roast
    if message.tool_calls:
        groq_messages.append(message)

        for tool_call in message.tool_calls:
            if tool_call.function.name == "get_strong_examples":
                args = json.loads(tool_call.function.arguments)
                result = get_strong_examples(args["dimension"])
                groq_messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result,
                })

        # Second call — LLM now has real examples, writes the roast
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=groq_messages,
            temperature=0.7,
            max_tokens=1024,
        )
        return response.choices[0].message.content

    return message.content
