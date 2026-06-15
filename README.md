# 🧪 Learning Promptfoo — A Hands-on Course

A multi-part, hands-on course for learning **[Promptfoo](https://www.promptfoo.dev/)** —
the open-source toolkit for **testing and evaluating LLM output** the way you'd
unit-test normal code.

Each part is a **self-contained mini-project**: its own config, prompts, code,
`requirements.txt`, and its own README telling you exactly how to run it. Start
at Part I and work forward — or jump straight to the topic you need.

---

## 📚 Course parts

| Part | Topic | Folder | Status |
|------|-------|--------|--------|
| **I** | **Assertions** — score model output with deterministic & model-graded checks | [`part1_assertions/`](part1_assertions/) | ✅ Ready |
| II | _Coming soon_ | — | 🚧 Planned |
| III | _Coming soon_ | — | 🚧 Planned |

> 👉 **New here? Start with [Part I →](part1_assertions/README.md)**

---

## 🤔 What is Promptfoo?

When you build with LLMs, "does it work?" isn't obvious — outputs vary, and a
prompt tweak that helps one case can quietly break another. Promptfoo lets you:

- Define **test cases** (inputs + what a good answer looks like)
- Run them against **one or many models** (OpenAI, Anthropic, local, …)
- **Score** each output automatically and compare side-by-side
- Catch regressions before they reach users

This course teaches those ideas one concept at a time.

---

## 🧰 Prerequisites

You need these once for the whole course:

| Tool | Why | Check |
|------|-----|-------|
| **Node.js 18+** | Promptfoo's CLI runs on Node (via `npx`, no install) | `node --version` |
| **Python 3.9+** | Some parts use custom Python graders/scripts | `python --version` |
| **An LLM API key** | To actually call a model | OpenAI or Anthropic |

Set your key once in your shell:

```bash
export OPENAI_API_KEY="sk-..."      # default provider used in the course
# or
export ANTHROPIC_API_KEY="sk-ant-..."
```

---

## 🚀 Quick start

```bash
# 1. (Optional) create a virtual environment
python -m venv .venv && source .venv/bin/activate

# 2. Install Python deps for ALL parts...
pip install -r requirements.txt
#    ...or just one part:
pip install -r part1_assertions/requirements.txt

# 3. Go into a part and follow its README
cd part1_assertions
```

Promptfoo itself needs **no install** — every part runs it with
`npx promptfoo@latest`, which fetches it on demand.

---

## 🗂 Repository layout

```
Practice_promptfoo/
├── README.md                 ← you are here (course overview)
├── requirements.txt          ← installs every part's Python deps
├── .gitignore
│
└── part1_assertions/         ← PART I — fully self-contained
    ├── README.md             ← how to run Part I
    ├── requirements.txt      ← Part I Python deps
    ├── promptfooconfig.yaml  ← the eval definition
    ├── prompts/              ← prompt templates
    ├── assertions/           ← custom Python graders
    ├── guide.html            ← illustrated step-by-step walkthrough
    └── .env.example
```

Each future part (`part2_…`, `part3_…`) follows the **same shape**, so once you
learn one, you know your way around all of them.

---

## 📖 How to use this course

1. Read this overview.
2. Open the part's folder and read **its** README.
3. (Part I also ships a visual `guide.html` — open it in a browser.)
4. Run the eval, inspect results, then tweak and re-run.

Happy evaluating! 🎉
