---
name: regex-builder
description: Write, explain, and test regular expressions. Use when the user needs to match, extract, validate, or replace text with a pattern, or asks what a regex does.
---

# Regex Builder

Help the user write correct, readable regular expressions and understand the ones they already have.

## Workflow

1. **Clarify intent.** Before writing anything, pin down:
   - 2–3 positive examples that must match.
   - 2–3 negative examples that must NOT match.
   - The regex dialect (JavaScript, Python, PCRE, POSIX, etc.).

2. **Write it.** Favor readability over cleverness:
   - Prefer explicit character classes over a broad `.` when the input is known.
   - Use a non-capturing group `(?:...)` unless a capture is actually consumed later.
   - Anchor with `^` / `$` when the whole string must match.

3. **Explain it.** For an existing regex, break it down token by token in plain language.

4. **Test it.** Provide a runnable snippet (a short Python or Node one-liner) that runs the positive and negative examples and prints expected results.

## Pitfalls to catch

- Unescaped metacharacters inside character classes.
- Greedy quantifiers matching too much — prefer `.*?` or a negated class.
- Forgetting that `.` does not match newlines in most engines.
- Catastrophic backtracking from nested quantifiers such as `(a+)+`.
