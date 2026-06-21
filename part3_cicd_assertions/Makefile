# Makefile — Part III CI/CD Integration
# Local developer commands that mirror what CI runs.
#
# Usage:
#   make security    → run security eval
#   make quality     → run quality eval
#   make eval        → run both
#   make view        → open the promptfoo web viewer
#   make clean       → delete output files
#   make install     → install Python deps

.PHONY: security quality eval view clean install check-key

# ── Check API key is set before running anything ─────────────────────────
check-key:
	@test -n "$$OPENAI_API_KEY" || (echo "ERROR: OPENAI_API_KEY not set. Run: export OPENAI_API_KEY=sk-..." && exit 1)

# ── Security eval (matches CI llm-security.yml) ──────────────────────────
security: check-key
	@echo "Running security evaluation..."
	bash scripts/run_eval.sh promptfooconfig.security.yaml

# ── Quality eval (matches CI llm-quality.yml) ────────────────────────────
quality: check-key
	@echo "Running quality evaluation..."
	bash scripts/run_eval.sh promptfooconfig.quality.yaml

# ── Run both pipelines ────────────────────────────────────────────────────
eval: security quality

# ── Open the interactive results viewer ──────────────────────────────────
view:
	npx promptfoo@latest view

# ── Parse the last results without re-running eval ───────────────────────
results:
	@python scripts/parse_results.py output/results.json

# ── Install Python dependencies ──────────────────────────────────────────
install:
	pip install -r requirements.txt

# ── Remove generated output files ────────────────────────────────────────
clean:
	rm -f output/*.json output/*.csv output/*.html
	find assertions -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
