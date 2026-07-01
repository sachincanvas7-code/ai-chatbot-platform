"""
RoastMyPM — backend (the "brain").

Step 1: a STATIC stub. It ignores the résumé and returns a fixed reply.
This proves the UI -> backend -> display loop works before we add any AI.

In Step 2 we'll replace the INSIDE of get_response() with a real LLM call.
The function's shape — takes text, returns text — stays the same the whole way.
"""


def get_response(resume_text):
    # Step 1: static placeholder (no LLM yet).
    return (
        "🔥 I'm RoastMyPM. My AI brain isn't wired up yet — that's Step 2. "
        "Right now I return this same message no matter what you paste, "
        "just to prove the plumbing works!"
    )
