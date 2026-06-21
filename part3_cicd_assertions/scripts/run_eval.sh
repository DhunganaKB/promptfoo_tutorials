#!/usr/bin/env bash
# scripts/run_eval.sh
#
# CI-friendly wrapper around `npx promptfoo eval`.
# Writes JSON output to output/results.json, then parses it for a
# human-readable summary. Exits non-zero if any test fails.
#
# Usage:
#   bash scripts/run_eval.sh [config_file]
#
# Examples:
#   bash scripts/run_eval.sh                              # defaults to security config
#   bash scripts/run_eval.sh promptfooconfig.quality.yaml

set -euo pipefail

CONFIG="${1:-promptfooconfig.security.yaml}"
OUTPUT_DIR="output"
OUTPUT_FILE="${OUTPUT_DIR}/results.json"

# ── Validate prerequisites ────────────────────────────────────────────────────
if [[ -z "${OPENAI_API_KEY:-}" ]]; then
  echo "ERROR: OPENAI_API_KEY is not set."
  echo "  Local:  export OPENAI_API_KEY='sk-...'"
  echo "  CI:     add it as a GitHub Actions secret"
  exit 1
fi

mkdir -p "$OUTPUT_DIR"

# ── Run eval ──────────────────────────────────────────────────────────────────
echo ""
echo "┌─────────────────────────────────────────────┐"
echo "│  promptfoo eval                             │"
echo "│  config : ${CONFIG}"
echo "│  output : ${OUTPUT_FILE}"
echo "└─────────────────────────────────────────────┘"
echo ""

# Flags:
#   --no-cache        always fresh API calls (critical in CI)
#   --max-concurrency cap parallel requests to avoid rate limits
#   --output          write JSON for parse_results.py
npx promptfoo@latest eval \
  --config  "$CONFIG" \
  --output  "$OUTPUT_FILE" \
  --max-concurrency 3 \
  --no-cache

echo ""
echo "Eval complete. Parsing results..."
echo ""

# ── Parse & exit ──────────────────────────────────────────────────────────────
python scripts/parse_results.py "$OUTPUT_FILE"
