# Part III — LLM Testing in CI/CD

> Automate promptfoo security and quality evaluations in GitHub Actions.
> Every prompt change, model upgrade, and PR gets tested automatically.

This part is **fully self-contained**. (For the course overview, see the [root README](../README.md).)

---

## 🗂 What's in this part

```
part3_cicd_assertions/
├── .github/workflows/
│   ├── llm-security.yml        # Security pipeline (push + PR + nightly)
│   └── llm-quality.yml         # Quality pipeline (matrix across models)
├── Makefile                    # Local dev commands
├── scripts/
│   ├── run_eval.sh             # CI-friendly eval wrapper
│   └── parse_results.py        # Parse JSON → summary + exit code
├── promptfooconfig.security.yaml   # 10 security test cases
├── promptfooconfig.quality.yaml    # 8 quality test cases
├── prompts/                    # Prompt templates
├── assertions/                 # Custom Python detectors
└── output/                     # JSON results (gitignored)
```

---

## ✅ Prerequisites

- **Node.js 18+** — `node --version`
- **Python 3.9+** — `python --version`
- **An OpenAI API key** — `export OPENAI_API_KEY="sk-..."`

---

## ▶️ Local development

```bash
cd part3_cicd_assertions

# Run security tests (mirrors CI)
make security

# Run quality tests
make quality

# Run both
make eval

# Open interactive viewer
make view

# Parse last results without re-running
make results
```

---

## 🔧 GitHub Actions setup

1. **Add your API key as a secret:**
   `GitHub repo → Settings → Secrets → Actions → New secret`
   Name: `OPENAI_API_KEY`, Value: `sk-...`

2. **Copy the `.github/` folder to your repo root:**
   ```bash
   cp -r .github/ ../../.github/
   ```

3. **Push to main or open a PR** — the workflows trigger automatically.

---

## 📊 What each pipeline does

| Pipeline | Trigger | Tests | On failure |
|----------|---------|-------|------------|
| `llm-security.yml` | push · PR · nightly | 10 security | Blocks merge, posts PR comment |
| `llm-quality.yml` | push · PR | 8 quality (matrix) | Blocks merge, posts PR comment |

---

## 🆘 Troubleshooting

| Symptom | Fix |
|---------|-----|
| `OPENAI_API_KEY not set` | `export OPENAI_API_KEY="sk-..."` |
| `npx` prompts to install | Type `y` — cached after first run |
| All tests pass instantly | Check `--no-cache` is in run_eval.sh |
| PR comment not posting | Ensure `pull-requests: write` permission in workflow |

➡️ Previous: [Part II — Security Testing](../part2_assertions/README.md)
