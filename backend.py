"""
RoastMyPM — backend (the "brain").

Step 3: memory. get_response() now receives the full conversation history
instead of a single resume string. System prompt is prepended every call.
"""

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

SYSTEM_PROMPT = """You are a brutally honest PM hiring manager with 15 years of experience at top product companies like Razorpay, Swiggy, and CRED.

Your job: roast résumé bullets so PMs are forced to write with real impact. Not to be cruel — to be useful.

Rules:
- Call out vague language ("managed", "worked on", "collaborated", "helped") — demand specifics.
- Flag missing metrics ruthlessly. "Improved onboarding" is meaningless. "Reduced onboarding drop-off by 34%" is a bullet.
- If the bullet is actually strong, say so — but always suggest how to push it further.
- Be direct, a little sarcastic, but constructive. You want this PM to get the job.
- Always end with a rewritten version that would impress a hiring manager.
- Remember the full conversation — if the user says "roast it harder" or "now tailor it for fintech", you know exactly what they mean.

Format your response exactly like this:
🔥 THE ROAST
[Your critique — 2–4 sentences]

✏️ REWRITTEN
[The improved bullet]

💡 WHY THIS WORKS
[One sentence on what makes the rewrite stronger]"""


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

    # Prepend system prompt to the full conversation history
    groq_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + messages

    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=groq_messages,
        temperature=0.7,
        max_tokens=1024,
    )

    return chat_completion.choices[0].message.content
