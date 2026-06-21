#!/usr/bin/env python3
"""
scripts/parse_results.py

Parse a promptfoo JSON output file, print a human-readable summary,
and exit with code 1 if any test failed — blocking the CI pipeline.

Usage:
    python scripts/parse_results.py output/results.json
    python scripts/parse_results.py output/results.json --format github
"""
import json
import sys
from pathlib import Path


# ── Loader ────────────────────────────────────────────────────────────────────

def load(path: str) -> dict:
    """Return the inner results dict from a promptfoo output file."""
    raw = json.loads(Path(path).read_text())
    # promptfoo wraps results under a top-level key in some versions
    inner = raw.get("results", raw)
    if isinstance(inner, dict) and "results" in inner:
        return inner
    return raw


# ── Summariser ────────────────────────────────────────────────────────────────

def summarise(data: dict) -> dict:
    stats        = data.get("stats", {})
    results_list = data.get("results", [])

    total_cost    = 0.0
    total_latency = 0
    failed        = []

    for r in results_list:
        total_cost    += r.get("cost", 0) or 0
        total_latency += r.get("latencyMs", 0) or 0

        if not r.get("success", True):
            grading = r.get("gradingResult", {}) or {}
            failed.append({
                "description": r.get("description")
                               or r.get("prompt", {}).get("label", "—"),
                "reason": (grading.get("reason") or
                           r.get("response", {}).get("error") or "")[:200],
                "score": r.get("score", 0),
            })

    n = len(results_list) or 1
    return {
        "successes":    stats.get("successes", 0),
        "failures":     stats.get("failures", 0),
        "total_tokens": stats.get("tokenUsage", {}).get("total", 0),
        "avg_latency":  round(total_latency / n),
        "total_cost":   round(total_cost, 6),
        "failed":       failed,
    }


# ── Printers ─────────────────────────────────────────────────────────────────

def print_terminal(s: dict) -> None:
    total   = s["successes"] + s["failures"]
    status  = "PASSED" if s["failures"] == 0 else "FAILED"
    W = 62

    print("\n" + "━" * W)
    print(f"  PROMPTFOO EVAL  ·  {status}")
    print("━" * W)
    print(f"  Tests    : {total}")
    print(f"  Passed   : {s['successes']:>4}  ✅")
    print(f"  Failed   : {s['failures']:>4}  {'❌' if s['failures'] else '—'}")
    print(f"  Tokens   : {s['total_tokens']:>6,}")
    print(f"  Avg latency : {s['avg_latency']:>5} ms")
    print(f"  Total cost  : ${s['total_cost']:.6f}")
    print("━" * W)

    if s["failed"]:
        print("\n  FAILURES\n")
        for f in s["failed"]:
            print(f"  ✗  {f['description']}")
            if f["reason"]:
                print(f"     → {f['reason']}")
            print()


def print_github(s: dict) -> None:
    """Markdown for GitHub Actions step summary (GITHUB_STEP_SUMMARY)."""
    total  = s["successes"] + s["failures"]
    icon   = "✅" if s["failures"] == 0 else "❌"
    status = "PASSED" if s["failures"] == 0 else "FAILED"

    lines = [
        f"## {icon} Promptfoo Eval — {status}",
        "",
        "| Metric | Value |",
        "|--------|-------|",
        f"| Tests | {total} |",
        f"| ✅ Passed | {s['successes']} |",
        f"| ❌ Failed | {s['failures']} |",
        f"| Tokens | {s['total_tokens']:,} |",
        f"| Avg latency | {s['avg_latency']} ms |",
        f"| Total cost | ${s['total_cost']:.6f} |",
    ]

    if s["failed"]:
        lines += ["", "### Failed Tests", ""]
        for f in s["failed"]:
            lines.append(f"- **{f['description']}** (score: {f['score']:.2f})")
            if f["reason"]:
                lines.append(f"  > {f['reason']}")

    print("\n".join(lines))


# ── Entry point ───────────────────────────────────────────────────────────────

def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("Usage: python scripts/parse_results.py <results.json> [--format github]")
        sys.exit(1)

    path          = args[0]
    github_format = len(args) > 2 and args[1] == "--format" and args[2] == "github"

    if not Path(path).exists():
        print(f"ERROR: results file not found: {path}")
        sys.exit(1)

    data = load(path)
    s    = summarise(data)

    if github_format:
        print_github(s)
    else:
        print_terminal(s)

    if s["failures"] > 0:
        print(f"\n  ❌ {s['failures']} test(s) failed — pipeline blocked.\n")
        sys.exit(1)

    print(f"\n  ✅ All {s['successes']} tests passed.\n")
    sys.exit(0)


if __name__ == "__main__":
    main()
