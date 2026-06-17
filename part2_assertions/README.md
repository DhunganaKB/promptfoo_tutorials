# Part II — LLM Vulnerability Detection

> Red-team your AI application with automated security tests.
> Covers **prompt injection, system prompt leakage, PII extraction, jailbreaking,** and **XSS/output injection**.

This part is **fully self-contained** — everything needed to run it lives in this folder.
(For the course overview, see the [root README](../README.md).)

---

## 🎯 What you'll learn

| Attack Category | What it tests |
|-----------------|---------------|
| **Prompt Injection** | Can user input override the system prompt? |
| **System Prompt Leakage** | Does the model expose internal configuration? |
| **PII Extraction** | Does the model leak or fabricate personal data? |
| **Jailbreaking** | Does the model comply with harmful requests? |
| **XSS / Output Injection** | Does unsafe input propagate unfiltered into output? |

---

## 📁 Files in this part

| File | Purpose |
|------|---------|
| `promptfooconfig.yaml` | 15 security test cases across 5 attack categories |
| `prompts/customer_support.txt` | The simulated target app (has fake secrets embedded) |
| `assertions/pii_detector.py` | Detects SSNs, emails, API tokens, DB hosts in output |
| `assertions/refusal_checker.py` | Verifies the model refused a harmful request |
| `requirements.txt` | Python deps (stdlib only — no install needed) |
| `.env.example` | API key template |
| `guide.html` | Full Medium-style article — open in a browser |

---

## ✅ Prerequisites

- **Node.js 18+** — `node --version`
- **Python 3.9+** — `python --version`
- An **OpenAI API key** (or Anthropic key)

---

## ▶️ How to run this part

```bash
# 1. Enter this folder
cd part2_assertions

# 2. Set your API key
export OPENAI_API_KEY="sk-..."

# 3. Run the security evaluation (15 tests)
npx promptfoo@latest eval

# 4. Open the interactive results viewer
npx promptfoo@latest view
# → http://localhost:15500
```

> No Python install needed for this part — both custom assertions use only stdlib.

---

## 📊 Reading the results

A **FAIL** here is actually good news — it means you caught a vulnerability.
A **PASS** means your model handled that attack correctly.

| Result | Meaning |
|--------|---------|
| 🟢 PASS | Model resisted the attack |
| 🔴 FAIL | Potential vulnerability — investigate and harden |
| Score 0.6 | Ambiguous — manual review needed |

---

## 🔧 Try it yourself

- Add a new injection test: copy an `[Injection-*]` block and craft a new attack.
- Lower `threshold` on the `latency` assertion to catch slow security responses.
- Swap the provider to Anthropic and compare how each model handles jailbreaks.
- Extend `pii_detector.py` to use `presidio-analyzer` for ML-based PII detection.

---

## 🆘 Troubleshooting

| Symptom | Fix |
|---------|-----|
| `OPENAI_API_KEY` not set | `export OPENAI_API_KEY="sk-..."` |
| Assertion file not found | Run `npx promptfoo eval` from **inside** `part2_assertions/` |
| `npx` prompts to install | Type `y` — it caches promptfoo locally |
| All tests pass instantly | Check your provider is actually making API calls (`--verbose`) |

➡️ Previous: [Part I — Assertions](../part1_assertions/README.md) | Next: Part III (coming soon)
