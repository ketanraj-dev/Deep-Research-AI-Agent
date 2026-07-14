# Deep / Research

> **Multi-agent web investigation** — ask any question, get a structured research report delivered to your inbox in seconds.

![Deep Research UI](https://img.shields.io/badge/UI-Gradio-orange?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.12%2B-blue?style=flat-square)
![uv](https://img.shields.io/badge/managed%20with-uv-de5fe9?style=flat-square)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?style=flat-square)
![Gemini](https://img.shields.io/badge/Google-Gemini-4285F4?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

---

## What it does

Type any research question. Deep/Research spins up a **pipeline of four specialised AI agents** that plan searches, scour the web in parallel, synthesise the findings into a well-structured report, and email you the result — all without you lifting another finger.

```
Your question
    │
    ▼
┌─────────────┐   structured   ┌──────────────┐  parallel   ┌──────────────┐
│ Planner     │─── search ────▶│ Search Agent │─ web calls ▶│  Live Web    │
│ Agent       │   queries      │ (×N)         │             │  (OpenAI)    │
│ (Gemini)    │                └──────────────┘             └──────────────┘
└─────────────┘                        │ summaries
                                       ▼
                              ┌──────────────┐
                              │ Writer Agent │  →  Markdown Report (~1 500 words)
                              │ (Gemini)     │
                              └──────────────┘
                                       │
                                       ▼
                              ┌──────────────┐
                              │ Email Agent  │  →  HTML email to your inbox
                              │ (Gemini)     │       (or Pushover notification)
                              └──────────────┘
```

---

## Features

- **Real-time progress stepper** — watch each phase light up as it completes
- **Parallel web searches** — N queries run concurrently for speed
- **Structured output** — reports follow a consistent heading hierarchy
- **One-click copy** — copy the full report to clipboard from the UI
- **Dark / Light mode** — toggle with the Theme button
- **Email or push notification** — choose SMTP delivery or Pushover
- **Fully configurable** — tweak model, provider, and search count via `.env`

---

## Quickstart

This project is managed with [**uv**](https://docs.astral.sh/uv/) — no manual virtualenv or `pip install` needed. If you don't have it yet:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh   # macOS / Linux
# Windows: powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 1 — Clone & install

```bash
git clone https://github.com/your-username/deep-research.git
cd deep-research

uv sync
```

`uv sync` creates a `.venv` and installs every dependency pinned in `uv.lock` — reproducible, no separate `pip install` step.

### 2 — Configure secrets

```bash
cp .env.example .env
# Edit .env and fill in your API keys (see Configuration section below)
```

### 3 — Run

```bash
uv run app.py
```

Open **http://localhost:7860** in your browser.

---

## Configuration

All settings live in `.env` (never commit this file — it is in `.gitignore`).

| Variable | Required | Description |
|---|---|---|
| `OPENAI_API_KEY` | Yes | Used by the **Search Agent** for live web browsing via `WebSearchTool` |
| `GOOGLE_API_KEY` | Yes | Used by **Planner**, **Writer**, and **Email** agents (Gemini) |
| `DEEPSEEK_API_KEY` | No | Optional alternative provider |
| `EMAIL_ADDRESS` | If `USE_EMAIL=true` | Sender & recipient address |
| `EMAIL_SMTP_SERVER` | If `USE_EMAIL=true` | e.g. `smtp.gmail.com` |
| `EMAIL_APP_PASSWORD` | If `USE_EMAIL=true` | Gmail App Password (not your login password) |
| `PUSHOVER_USER` | If `USE_EMAIL=false` | Pushover user key |
| `PUSHOVER_TOKEN` | If `USE_EMAIL=false` | Pushover application token |
| `HOW_MANY_SEARCHES` | No | Number of parallel searches per query (default `3`) |
| `USE_EMAIL` | No | `true` → SMTP, `false` → Pushover (default `true`) |

### Getting a Gmail App Password

1. Enable 2-factor authentication on your Google account.
2. Go to **Google Account → Security → App passwords**.
3. Create a new app password, paste it into `.env` as `EMAIL_APP_PASSWORD`.

---

## Project structure

```
deep_research/
├── app.py               # Gradio UI — entry point
├── styles.py            # All CSS, JS, HTML for the UI
├── config.py            # Provider config (reads from .env)
├── models.py            # OpenAI-compatible client factory
├── research_manager.py  # Orchestrates the four-agent pipeline
├── planner_agent.py     # Breaks the query into N search queries
├── search_agent.py      # Executes one web search and summarises
├── writer_agent.py      # Synthesises summaries into a full report
├── email_agent.py       # Formats and sends the HTML email
├── messenger.py         # SMTP + Pushover helpers
├── .env.example         # Template — copy to .env and fill in keys
├── .gitignore           # Keeps secrets and caches out of git
├── pyproject.toml       # Project metadata & dependencies
└── uv.lock              # Locked, reproducible dependency versions
```

---

## How the agents work

### Planner Agent *(Gemini)*
Receives the raw user query and returns `HOW_MANY_SEARCHES` targeted search queries, each with a reason explaining its relevance.

### Search Agent *(GPT-4o-mini + WebSearchTool)*
Executes **one** search query against the live web and returns a concise 2–3 paragraph summary. Multiple instances run in parallel.

### Writer Agent *(Gemini)*
Reads all summaries and synthesises them into a single ~1 500-word markdown report with clear headings, stats, comparisons, and follow-up questions.

### Email Agent *(Gemini)*
Converts the markdown report into a well-formatted HTML email (or a Pushover notification) and dispatches it.

---

## Extending the project

**Add a dependency**

```bash
uv add some-package
```

This updates `pyproject.toml` and `uv.lock` together — no need to touch either by hand.

**Add a new LLM provider**

Edit `config.py` — add an entry to `PROVIDER` with the provider name, API key, and base URL. Then call `get_model("your-provider", "model-name")` in any agent file.

**Change the search model**

Open `search_agent.py` and update `MODEL_NAME`. The search agent uses the OpenAI SDK directly and requires a model that supports `WebSearchTool`.

**Increase parallel searches**

Set `HOW_MANY_SEARCHES=5` (or higher) in `.env`. Each extra search adds a parallel web call with no code changes needed.

---

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) for dependency management
- An OpenAI API key with access to `gpt-4o-mini`
- A Google AI Studio (Gemini) API key
- (Optional) A Gmail account with App Passwords enabled, or a Pushover account

---

## License

MIT — do whatever you like, attribution appreciated.

---

*Built with [OpenAI Agents SDK](https://github.com/openai/openai-agents-python), [Gradio](https://gradio.app/), and the Gemini API.*
