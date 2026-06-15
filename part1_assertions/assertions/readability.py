"""
Custom Python assertion for promptfoo.

Promptfoo calls `get_assert(output, context)` for every test that uses:

    - type: python
      value: file://assertions/readability.py

`output`  -> the model's text response (str)
`context` -> dict with the test's vars, prompt, provider, etc.

Return one of: a bool, a 0.0-1.0 float (score), or a GradeResult dict
like the one below. This example grades how *easy to read* the answer is
using the Flesch-Kincaid grade level (lower = simpler). It demonstrates
why we need a requirements.txt: it depends on the `textstat` package.
"""

import textstat

# An answer aimed at a general audience should read at roughly a
# 9th-grade level or below. Tune this for your use case.
MAX_GRADE_LEVEL = 9.0


def get_assert(output: str, context: dict):
    grade = textstat.flesch_kincaid_grade(output)
    passed = grade <= MAX_GRADE_LEVEL
    return {
        "pass": passed,
        "score": 1.0 if passed else 0.0,
        "reason": (
            f"Flesch-Kincaid grade level {grade:.1f} "
            f"(target ≤ {MAX_GRADE_LEVEL})"
        ),
    }
