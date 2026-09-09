---
name: skill-scaffold
description: Scaffold a new ClawHub-ready skill folder with the required SKILL.md frontmatter, references/ dir, and skill-card.md in one step. Use when you need a clean, publishable skill skeleton without hand-writing boilerplate.
metadata:
  clawdbot:
    emoji: "🧱"
    tags:
      - scaffold
      - skill
      - cli
    version: "1.0.0"
    license: MIT
---

# skill-scaffold

Create a new skill folder ready for `clawhub publish`.

## When to use

- You want to publish a new skill but don't want to hand-write the frontmatter boilerplate.
- You need a consistent, minimal skill layout (SKILL.md + references/ + skill-card.md).

## Prerequisites

- `clawhub` CLI installed (`npm i -g clawhub`).
- A logged-in publisher (`clawhub whoami` returns your handle).

## Steps

1. Decide a slug (lowercase, hyphenated, e.g. `my-utility-skill`).
2. Create the folder and files using the commands below.
3. Edit `SKILL.md` body and `skill-card.md` to describe your skill.
4. Validate with a dry-run publish, then publish for real.

## Commands

```bash
SLUG="my-utility-skill"
mkdir -p "./${SLUG}/references"

# SKILL.md with required frontmatter
cat > "./${SLUG}/SKILL.md" <<'EOF'
---
name: my-utility-skill
description: One-line description of what the skill does and when to use it.
metadata:
  clawdbot:
    emoji: "🧩"
    tags: [utility]
    version: "1.0.0"
    license: MIT
---

# my-utility-skill

Describe the skill here. Include when to use it, prerequisites, and steps.
EOF

# skill-card.md (publisher-facing card)
cat > "./${SLUG}/skill-card.md" <<'EOF'
## Description:

One-line description.

## Publisher:

[your-handle](https://clawhub.ai/user/your-handle)

## Use Case:

Who uses this and why.

## Reference(s):

- [references/example.md](references/example.md)
EOF

# placeholder reference
cat > "./${SLUG}/references/example.md" <<'EOF'
# Example reference

Put supporting docs, templates, or scripts here.
EOF

# Dry-run, then publish
clawhub publish "./${SLUG}" --slug "${SLUG}" --name "My Utility Skill" --version 1.0.0 --tags utility
```

## Output

A folder named after the slug containing `SKILL.md`, `skill-card.md`, and `references/`.
After `clawhub publish`, the skill appears under your publisher handle on ClawHub.

## Notes

- Keep `description` under ~200 chars; it shows in search results.
- The `version` must be a valid SemVer string and should bump on every republish.
- Use `--dry-run` first to confirm fingerprint and file count before a real publish.
