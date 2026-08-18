---
name: skill-name
description: "Clear, specific description of what this skill does and when to use it. Include trigger keywords."
version: "1.0.0"
author: "Author name"
compatibility: "Any runtime requirements"
metadata:
  created: "YYYY-MM-DD"
  updated: "YYYY-MM-DD"
  quality-score: "XX/50"
---

# Skill Name [Emoji]

One-line summary of what this skill does.

## When to Use

- Trigger 1: "specific phrase user might say"
- Trigger 2: "another common phrasing"
- Trigger 3: "edge case trigger"

**Don't use when:**
- Negative trigger 1
- Negative trigger 2

## Overview

Brief context: why this skill exists, what problem it solves, key principles.

## Prerequisites

| Dependency | Version | Install | Verify |
|-----------|---------|---------|--------|
| Tool X | >= 2.0 | `npm install -g tool-x` | `tool-x --version` |
| API Key Y | — | See TOOLS.md | `echo $API_KEY` |

## Workflow

### Step 1: [Action Verb] [Object]

**Action:** What to do
**Input:** What's needed
**Expected output:** What success looks like
**Verify:** How to confirm it worked

```bash
# Example command
command --flag argument
```

### Step 2: [Action Verb] [Object]

**Action:** What to do
**Input:** What's needed
**Expected output:** What success looks like
**Verify:** How to confirm it worked

### Step 3: [Action Verb] [Object]

...

## Error Handling

| Error | Cause | Solution | Prevention |
|-------|-------|----------|------------|
| `Error X` | Missing dependency | `install dep` | Check prerequisites |
| `Error Y` | Invalid input | Validate input | Add input check in Step 1 |

## Examples

### Example 1: [Common Use Case]

**Context:** [When would someone need this?]
**Input:** [What they provide]
**Process:** [What the skill does]
**Output:** [What they get]

```
# Concrete example
$ command --example
result: ...
```

### Example 2: [Edge Case]

...

## Output Specification

| Output | Format | Location | Verification |
|--------|--------|----------|--------------|
| File X | Markdown | `path/to/file` | `cat file \| head` |
| Report Y | PDF | `path/to/report` | Open in browser |

## Related Skills

- [skill-a](../skill-a/SKILL.md) — Does X, use before this skill
- [skill-b](../skill-b/SKILL.md) — Does Y, use after this skill

## References

- [Documentation](https://example.com)
- [Paper](https://arxiv.org/...)
- [GitHub](https://github.com/...)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | YYYY-MM-DD | Initial version |
