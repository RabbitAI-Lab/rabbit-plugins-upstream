---
name: skill-radar
description: |
  Meta-skill that acts as a routing layer for multi-skill agents. When installed,
  it intercepts user queries BEFORE other skills are loaded, scores all available
  skills using declarative routing rules, and instructs the agent to load ONLY the
  top-matching skills into context. This dramatically reduces system prompt bloat
  and improves skill dispatch accuracy. Zero ML infrastructure required.
compatibility: Python 3.10+, PyYAML. Framework-agnostic (WorkBuddy, Claude Code, Codex, OpenClaw, Hermes, or any custom agent).
metadata:
  author: ninetyhe-90
  version: "1.1.0"
  category: agent-infrastructure
  tags: [routing, skill-management, multi-skill, dispatch, meta-skill]
---

# Skill Radar — Declarative Skill Routing Engine

## What this skill does

When you (the agent) receive a user query, **do NOT load all available skills at once**. Instead, follow the execution protocol below to route the query to only the most relevant skill(s).

---

## Execution Protocol (D-mode: self-routing)

**You MUST follow these steps for every user query when this skill is active:**

### Step 0: Check if routing is needed

Skip routing if:
- The user explicitly names a skill (e.g., "use the pdf skill")
- The query is a simple greeting or meta-question about you
- There are fewer than 4 skills installed

Otherwise, proceed to Step 1.

### Step 1: Run the router

Execute the routing script with the user's query:

```bash
python3 {SKILL_DIR}/skill_radar/cli.py route "{USER_QUERY}" --skills-dir {SKILLS_DIR} --format json
```

Where:
- `{SKILL_DIR}` = the directory where this skill (skill-radar) is installed
- `{SKILLS_DIR}` = the directory containing all other skills (each with a `routing.yaml`)
- `{USER_QUERY}` = the user's raw input text

### Step 2: Read the output

The script returns JSON:

```json
{
  "query": "review this contract for risks",
  "results": [
    {"skill": "contract-review", "score": 0.41, ...},
    {"skill": "code-review", "score": 0.12, ...}
  ],
  "excluded": [
    {"skill": "some-skill", "reason": "anti_pattern: draft a contract"}
  ]
}
```

### Step 3: Load only matched skills

- If `results` is non-empty: load ONLY the skills listed in `results` (by name). Do NOT load other skills.
- If `results` is empty: fall back to your default skill loading behavior (load all, or use your own heuristic).
- If the script fails to run: fall back to default behavior. Never block the user.

### Step 4: Proceed normally

With the filtered skill set loaded, respond to the user's query as usual.

---

## Integration Modes

This skill supports **4 integration modes** to work with any agent framework:

### Mode D: Self-routing (recommended for ClawHub/OpenClaw/WorkBuddy)

The agent itself runs the routing script as described above. No framework changes needed — just install this skill and it provides routing instructions that the agent follows.

### Mode A: CLI (for any framework with shell access)

```bash
# Install
pip install skill-radar   # or: pip install -e /path/to/skill-radar

# Route a query
skill-radar route "review this contract" --skills-dir ./skills/ --format json
```

The framework calls this command before assembling the system prompt, and only includes the returned skills.

### Mode B: Python SDK (for Python-based agents)

```python
from skill_radar import load_skills

router = load_skills("~/.workbuddy/skills/")
results = router.route("review this contract")
# results = [ScoringResult(skill_name="contract-review", score=0.41, ...)]

# Only load these skills into your prompt:
skills_to_load = [r.skill_name for r in results]
```

### Mode C: HTTP microservice (for cloud-based agents)

```bash
skill-radar serve --skills-dir ./skills/ --port 8900
```

Then from your agent framework:
```
POST http://localhost:8900/route
Body: {"query": "review this contract", "context": {"file_types": [".docx"]}}
```

---

## Setup: Adding routing declarations to your skills

Each skill needs a `routing.yaml` file declaring when it should trigger:

```yaml
name: contract-review
description: "Legal contract review and risk analysis"

routing:
  keywords:
    - "contract review"
    - "review contract"
    - "NDA"
    - "agreement audit"
  patterns:
    - "(review|check|audit).{0,8}(contract|agreement|NDA|terms)"
    - "(contract|agreement).{0,6}(review|check|risk)"
  anti_patterns:
    - "draft a contract"
    - "contract template"
  priority: 80
  context:
    file_types: [".docx", ".pdf"]
```

### Auto-generate routing.yaml

For skills that don't have routing declarations yet:

```bash
skill-radar init --skills-dir ./skills/
```

This scans each skill's SKILL.md and auto-generates a basic `routing.yaml` from its metadata (name, description, trigger keywords).

---

## Scoring Formula

```
Score(q, skill) = 0.30 × keyword_hit_ratio
               + 0.25 × pattern_matched
               + 0.15 × intent_match
               + 0.15 × context_bonus
               + 0.15 × (priority / 100)
               - anti_pattern_penalty
```

Anti-pattern hit = immediate exclusion (score forced to 0).

Threshold strategy (default: gap-based):
- If top-1 score leads top-2 by > 0.15 → only load top-1
- Otherwise → load all skills scoring above 0.30

---

## File Structure

```
skill-radar/
├── SKILL.md                          ← This file (meta-skill instructions)
├── pyproject.toml                    ← Python package definition
├── skill_radar/                      ← Python package
│   ├── __init__.py                   ← SDK entry point
│   ├── core.py                       ← Framework-agnostic routing engine
│   ├── loader.py                     ← File system skill loading
│   ├── cli.py                        ← CLI entry point (route/init/serve)
│   ├── init_routing.py               ← Auto-generate routing.yaml
│   └── server.py                     ← HTTP server
├── references/
│   ├── scoring-theory.md             ← Mathematical foundations
│   └── routing-schema.md             ← Full YAML schema spec
├── assets/
│   └── skill-routing-config-template.yaml
└── examples/                         ← 6 cross-domain example skills
```

---

## Important Notes

- This skill should be loaded with HIGH priority (it gates other skill loading)
- If routing script execution fails, ALWAYS fall back to default behavior — never block the user
- The routing decision is transparent: the JSON output includes matched keywords/patterns for auditability
- Skills without `routing.yaml` are invisible to the router — they will only load via fallback
- Routing adds ~50ms latency per query (regex matching, no network calls)
