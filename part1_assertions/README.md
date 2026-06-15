# Part I — Assertions

> Score LLM output with **deterministic** and **model-graded** assertions.
> Based on the [“Promptfoo Assertions Overview”](https://www.youtube.com/watch?v=jpY8ECnAosU) video.

This part is **fully self-contained** — everything you need to run it lives in
this folder. (For the big-picture course overview, see the
[root README](../README.md).)

---

## 🎯 What you'll learn

An **assertion** is a single automated check on a model's answer. A test passes
only when **all** its assertions pass. Two families:

| Family | How it judges | Cost | Examples |
|--------|---------------|------|----------|
| **Deterministic** | Pure code — fast & repeatable | Free | `contains`, `regex`, `is-json`, `javascript`, `python`, `latency`, `cost` |
| **Model-graded** | Another model / embeddings judges meaning & quality | Small | `llm-rubric`, `similar`, `g-eval`, `factuality` |

This part demonstrates **all of the above** in one runnable config, including a
**custom Python grader** (`assertions/readability.py`) — which is exactly why
this part has its own `requirements.txt`.

---

## 📁 Files in this part

| File | Purpose |
|------|---------|
| `promptfooconfig.yaml` | The eval definition: prompts, providers, tests, assertions |
| `prompts/assistant.txt` | Prompt template (uses `{{question}}`) |
| `assertions/readability.py` | Custom Python grader (needs `textstat`) |
| `requirements.txt` | Python dependencies for this part |
| `.env.example` | API-key template |
| `guide.html` | Illustrated step-by-step walkthrough — open in a browser |

---

## ✅ Prerequisites

- **Node.js 18+** (`node --version`) — promptfoo runs via `npx`, no install
- **Python 3.9+** (`python --version`) — for the custom grader
- An **OpenAI API key** (default) or Anthropic key

---

## ▶️ How to run this part

```bash
# 1. Enter this folder
cd part1_assertions

# 2. (Recommended) create & activate a virtual environment
python -m venv .venv && source .venv/bin/activate

# 3. Install this part's Python dependencies
pip install -r requirements.txt

# 4. Set your API key
export OPENAI_API_KEY="sk-..."        # or copy .env.example -> .env

# 5. Run the evaluation
npx promptfoo@latest eval

# 6. Open the interactive results viewer (http://localhost:15500)
npx promptfoo@latest view
```

> 💡 **Prefer a guided walkthrough?** Open **`guide.html`** in your browser for
> the same steps with explanations and copy-paste buttons.

---

## 📊 Reading the results

`eval` prints a pass/fail grid and a summary (e.g. `Passed: 10  Failed: 1`).
In the web viewer, click any cell to see the full output and **which assertion
passed or failed** — including the grader's reasoning for model-graded ones.

- 🟢 **PASS** — every assertion in that test passed
- 🔴 **FAIL** — at least one failed (the reason is shown inline)
- **Score** — model-graded asserts return `0.0–1.0`; thresholds decide pass/fail

> ⚠️ Model-graded results aren't perfectly deterministic — a borderline case may
> occasionally flip. Loosen the rubric or lower the threshold to stabilize.

---

## 🔧 Try it yourself

- Change a `value` so a test **fails** on purpose, and watch the viewer explain why.
- Switch provider to Anthropic: in `promptfooconfig.yaml`, comment the `openai:`
  line, uncomment the `anthropic:` line, and set `ANTHROPIC_API_KEY`.
- Edit `assertions/readability.py` — lower `MAX_GRADE_LEVEL` and re-run.
- Run a subset: `npx promptfoo@latest eval --filter-pattern "json"`

---

## 🆘 Troubleshooting

| Symptom | Fix |
|---------|-----|
| `ModuleNotFoundError: textstat` | Run `pip install -r requirements.txt` (and activate your venv) |
| `OPENAI_API_KEY` errors | `export OPENAI_API_KEY="sk-..."` before running |
| Python assertion not found | Run `npx promptfoo eval` from **inside** `part1_assertions/` |
| `npx` prompts to install | Type `y` — it caches promptfoo for next time |

➡️ Next: Part II (coming soon). See the [course overview](../README.md).
