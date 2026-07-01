"""
RoastMyPM — database layer.

Creates a SQLite DB (roastmypm.db) and seeds it with curated strong/weak
PM résumé bullet examples. Called once on app startup via init_db().
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "roastmypm.db")

SEED_DATA = [
    # (dimension, quality, bullet)

    # metrics — numbers, percentages, business impact
    ("metrics", "strong", "Grew checkout conversion from 61% to 79% by redesigning the payment flow — adding Rs. 2.1 Cr in monthly GMV"),
    ("metrics", "strong", "Reduced customer support tickets by 43% in 90 days by shipping a self-serve cancellation flow"),
    ("metrics", "weak",   "Improved key metrics across the platform"),
    ("metrics", "weak",   "Worked on improving conversion for the checkout funnel"),

    # action — strong vs weak verbs
    ("action", "strong", "Spearheaded 0→1 build of a B2B onboarding module, cutting time-to-first-value from 14 days to 3"),
    ("action", "strong", "Overhauled the returns flow end-to-end, eliminating 3 redundant steps and cutting processing time by 60%"),
    ("action", "weak",   "Helped with the onboarding module development"),
    ("action", "weak",   "Worked on various initiatives across the product"),

    # scope — team size, budget, complexity
    ("scope", "strong", "Led a cross-functional squad of 12 (3 engineers, 2 designers, QA, data, legal) to ship India's first UPI-linked BNPL product"),
    ("scope", "strong", "Owned the full roadmap for a Rs. 80 Cr revenue line, prioritising across 4 competing stakeholder groups"),
    ("scope", "weak",   "Managed a team and worked on the product roadmap"),
    ("scope", "weak",   "Collaborated with stakeholders across different teams"),

    # ownership — accountability vs participation
    ("ownership", "strong", "Sole PM accountable for 0→1 launch of the merchant dashboard — from discovery to GA in 11 weeks"),
    ("ownership", "strong", "Took full ownership of the pricing model redesign, driving alignment across sales, finance, and engineering"),
    ("ownership", "weak",   "Assisted the team in launching the new dashboard feature"),
    ("ownership", "weak",   "Participated in pricing discussions and helped implement changes"),

    # outcome — result vs activity
    ("outcome", "strong", "Shipped real-time delivery tracking that lifted NPS by 18 points and reduced 'where is my order' calls by 55%"),
    ("outcome", "strong", "Launched smart nudge campaigns that re-engaged 34% of dormant users in 30 days, generating Rs. 45L incremental revenue"),
    ("outcome", "weak",   "Worked on a project to improve customer experience"),
    ("outcome", "weak",   "Delivered the new feature on time and within budget"),
]


def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS examples (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            dimension TEXT NOT NULL,
            quality   TEXT NOT NULL,
            bullet    TEXT NOT NULL
        )
    """)
    # Only seed if empty — safe to call on every app startup
    c.execute("SELECT COUNT(*) FROM examples")
    if c.fetchone()[0] == 0:
        c.executemany(
            "INSERT INTO examples (dimension, quality, bullet) VALUES (?, ?, ?)",
            SEED_DATA,
        )
    conn.commit()
    conn.close()


def get_strong_examples(dimension: str) -> str:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "SELECT quality, bullet FROM examples WHERE dimension = ?",
        (dimension,),
    )
    rows = c.fetchall()
    conn.close()

    if not rows:
        return f"No examples found for dimension: {dimension}"

    strong = [row[1] for row in rows if row[0] == "strong"]
    weak   = [row[1] for row in rows if row[0] == "weak"]

    result  = f"Curated examples for dimension '{dimension}':\n\n"
    result += "STRONG (what good looks like):\n"
    for b in strong:
        result += f"• {b}\n"
    result += "\nWEAK (what to avoid):\n"
    for b in weak:
        result += f"• {b}\n"

    return result
