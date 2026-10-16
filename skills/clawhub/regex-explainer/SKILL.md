---
name: regex-explainer
description: >
  Explain a regular expression in plain language and call out likely bugs.
  Use when the user pastes a regex they do not fully understand.
---

# Regex Explainer

## Purpose / Overview
Walks a regex token-by-token and notes greediness / anchors / groups.

## When to Use
Debugging validation, log parsers, or search patterns.

## Usage / Instructions
1. Ask for the regex and the flavor (JS/PCRE/Python) if relevant.
2. Explain groups, quantifiers, and character classes.
3. Give one matching and one non-matching example string.

## Examples
Input: `^\d{3}-\d{2}$`
Output: start, three digits, hyphen, two digits, end; matches `123-45`.

## Requirements / Dependencies
None.

## Limitations / Caveats
Does not execute against user files unless asked.

## Security / Permissions
Text-only.

## Attribution / License
MIT-0
