---
name: persistent-skill-memory
description: >
  Stops an agent from forgetting the skills it has installed. Auto-generates a categorized
  capability index from every installed SKILL.md's frontmatter and injects it into the
  durable system prompt between stable markers, with hooks so installing, inventing, or
  restoring a skill re-indexes automatically. Use when an agent has many skills but
  "forgets" they exist, when skills must survive context resets or sandbox snapshot wipes,
  or when you want one always-current answer to "what can I actually do?".
metadata: {"openclaw":{"emoji":"🧠"}}
---

# Persistent Skill Memory

Field-authored in Arena Agent Mode (2026-07) managing a 180-skill workspace.

## The problem

Installing skills to disk does **not** make an agent aware of them. Filesystem presence is
not memory: the agent must re-discover them every session, and after a context reset or a
snapshot wipe it behaves as if the skills were never installed. Symptoms:

- Solving from scratch a problem an installed skill already covers.
- Skill count grows, but effective capability doesn't.
- "What can you do?" gets a vague answer that ignores 170 installed skills.

## The fix: index → inject → auto-refresh

**1. Index.** Walk every `SKILL.md`, parse YAML frontmatter `name` + `description`
(handling `>` and `|` block scalars), fall back to the first `#` heading, dedupe by
`(owner, slug)` since one skill can land under multiple paths.

**2. Categorize.** Keyword-bucket into ~10 domains so lookup is by *need*, not by memorized
name. A flat 180-item list is unusable; grouped, it's scannable.

**3. Compress.** Full descriptions blow the prompt budget. The durable prompt gets
**names only, grouped by category** (~4.4 KB for 180 skills); full descriptions live in
`SKILLS_INDEX.md`, loaded on demand. Names are enough to trigger recall — the skill's own
SKILL.md is read before deep use.

**4. Inject between stable markers** so regeneration is idempotent and never duplicates:

```
<<<SKILL_INDEX_BEGIN>>>
[Anti-stall / async] durable-task-runner, polling-best-practices, ...
[Agents / orchestration] agent-team-orchestration, ...
<<<SKILL_INDEX_END>>>
```

Base standing directives live **above** the markers and are rewritten verbatim each time,
so behavioral rules and the capability list can never drift apart.

**5. Auto-refresh via hooks** — the part people skip, and why indexes go stale:

| Event | Hook |
|---|---|
| Installing a skill | `skill_add.sh` wrapper: install, then re-index |
| Publishing an invention | tail of `publish_inventions.sh` |
| Restoring after a wipe | tail of `restore_volatile.sh` |

Manual indexing rots within days. Hooked indexing stays true.

## Verification that actually proves it

Don't trust "the file was written". Install a new skill through the wrapper, then grep the
**live** prompt for its name:

```bash
./skill_add.sh @owner/new-skill
python3 manage_system_prompt.py show | grep -q "@owner/new-skill" && echo REMEMBERED
```

## Design rules

1. Names in the prompt, descriptions on disk — respect the budget.
2. Group by problem domain, never alphabetically only.
3. Markers, not appends — regeneration must be idempotent.
4. Dedupe by `(owner, slug)`.
5. Hook every mutation path; a manual step will be forgotten.
6. Regenerate the whole prompt from a single source of truth.
7. Prove it end-to-end against the live prompt, not the file.
