# RoastMyPM — Vision & Roadmap

> The north star for this project. Build v1 simple; everything below is the end goal.
> Specs may evolve, but the identity does not: **it's always "the résumé tool, just deeper."**

---

## 🎯 Vision (north star)
**RoastMyPM** — the brutally honest, free résumé coach for product managers.
Paste your résumé + a target role → get an **ATS score**, a **brutal-but-fair critique**
against a real PM rubric, and **rewritten bullets**, grounded in **what real PM roles
actually want** — with a bring-your-own-key option, transparent reasoning, and version
tracking. Built to be shared in the PM community (and to double as proof I can ship AI products).

**Principles:** free to use (Groq/Llama default + BYOK) · copyright-clean data only · each phase
ships on its own · simple first, deepen later.

---

## 🪜 Capability roadmap (each phase ships; none pivots)

| Phase | Capability | Tools / APIs | DB / Data | Enhancement(s) introduced | New concept |
|------|-----------|--------------|-----------|---------------------------|-------------|
| **v1** Core Roast | honest critique + rewrites; remembers the chat | LLM only | tiny SQLite: strong/weak PM bullet examples + rubric | **Groq/Llama default** (free, no card) + **BYOK** (model-agnostic) | UI, LLM, memory, system prompt, tool+DB |
| **v2** ATS Score | objective score + missing keywords | `compute_ats_score()` (internal) + **LanguageTool** (grammar/clarity) | keyword bank | **Token + cost meter**, **streaming + "show the LLM thinking"** | real tool, streaming |
| **v3** Tailor-to-Role | tailor roast to a specific JD | `fetch_job_description(url)` + **Wikipedia** (company background) | — | **Transparency panel**, **rate-limiting** | external-API tool |
| **v4** Real-Roles Intelligence | "what PM roles actually want" + salary reality | **Arbeitnow / Adzuna** jobs + salary, **O*NET** skills | **DB of real PM JDs** (from job platforms) | **Prompt caching** (cost control) | data ingestion / bigger DB |
| **v5** Grounded Advice (RAG) | cites best-practice résumé/PM guidance | embeddings + retrieval | **RAG corpus**: PM career guides + my CuriousPM notes | **Eval harness** (quality test), reasoning trace | RAG |
| **v6** Versions & Memory | save versions, track score improvement | — | persistent store | **Persistent memory** (across sessions) | persistence |

---

## 🔧 Enhancements ledger (where each lands)
| Enhancement | Phase | What it does |
|---|---|---|
| Free default (Gemini) + **BYOK** | v1 | Zero-cost public use; users plug their own key |
| **Model-agnostic backend** (Groq/OpenAI/Claude) | v1 | Auto-detect provider from key prefix |
| **Token + cost meter** | v2 | Tokens + ₹ per message — unit-economics signal |
| **Streaming + "show the LLM thinking"** | v2 | Word-by-word output + live reasoning/steps log |
| **Transparency panel** | v3/v4 | "scored against these criteria / using these JDs" — auditability brand |
| **Rate-limiting per session** | v3 | Abuse-proof + keeps the public demo free |
| **Prompt caching** | v4 | Cheap repeated context at scale |
| **Eval harness** | v5 | Test résumés + expected scoring → prove quality |
| **Persistent memory** | v6 | Remembers you across visits |

---

## 🌐 External APIs in the end goal (beyond the LLM)
Kept explicitly as part of the vision. All free + copyright-clean.

| External API | Powers | Phase | Key? | Note |
|---|---|---|---|---|
| **Web fetch** (`fetch_job_description(url)`) | tailor to a specific posting | v3 | ❌ | fetches a URL you provide |
| **Wikipedia API** | target-company background | v3 | ❌ | CC BY-SA (attribute) |
| **LanguageTool API** | grammar / clarity / passive-voice check | v2–v3 | ❌ free tier | open-source |
| **Arbeitnow Jobs API** | real PM JDs ("what roles want") | v4 | ❌ | employer/ATS-sourced |
| **Adzuna Jobs + Salary** | PM JDs + salary benchmarks (India) | v4 | ⚠️ free key | official API |
| **O*NET** (US Dept of Labor) | map résumé skills → in-demand skills | v4–v5 | ⚠️ free key | public domain |
| *(optional)* Resume-parser (Affinda/Skima) | structured extraction | opt | ⚠️ free key | LLM can do this instead |

🚫 **Excluded (ToS + copyright):** Glassdoor / LinkedIn / Indeed direct scraping. Arbeitnow/Adzuna give the same value, cleanly.

---

## 🟢 v1 scope (the first chatbot — simple, a true slice)
Covers all 6 Week-4 concepts; everything above is later.
- **UI** — paste résumé/bullet + chat (Streamlit)
- **LLM** — Groq/Llama free default (no card needed) + BYOK
- **Memory** — "rewrite that harder", "roast it again"
- **System prompt** — brutal-but-fair PM hiring-manager persona + rubric
- **Tool + DB** — `get_strong_examples(dimension)` → tiny SQLite of strong/weak PM bullets
- **Ship** — Streamlit Community Cloud, push-to-deploy (Pattern A)

---

## Notes / open items
- Repo currently named `ai-chatbot-platform` — consider renaming to `roastmypm` before going public (Sachin's call).
- Build order & per-step workflow: see the portfolio's `BUILD_PLAN.md` and `PROGRESS.md`.
- Stay in the build-it-myself model: Claude coaches; Sachin writes & commits each step.
