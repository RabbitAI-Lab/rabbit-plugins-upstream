# Skill Radar

**Declarative skill routing engine for multi-skill AI agents.**

When your agent has 10+ skills, stuffing all their descriptions into the system prompt causes token bloat and attention dilution. Skill Radar solves this by routing each user query to only the relevant skills — using author-declared rules, not embeddings.

## Quick Start

### Install

```bash
pip install skill-radar
# or install from source:
pip install -e /path/to/skill-radar
```

### Add routing declarations to your skills

Each skill needs a `routing.yaml`:

```yaml
name: my-skill
routing:
  keywords: ["keyword1", "keyword2"]
  patterns: ["(pattern).{0,6}(match)"]
  anti_patterns: ["should not trigger"]
  priority: 70
```

Or auto-generate them:

```bash
skill-radar init --skills-dir ./my-skills/
```

### Route a query

```bash
skill-radar route "review this contract for risks" --skills-dir ./my-skills/ --format json
```

Output:
```json
{
  "query": "review this contract for risks",
  "results": [{"skill": "contract-review", "score": 0.41}]
}
```

---

## Integration Modes

Skill Radar is **framework-agnostic**. It works with any agent system:

| Mode | Best for | How it works |
|------|----------|-------------|
| **D: Self-routing** | ClawHub, OpenClaw, WorkBuddy, CodeBuddy | Install as a skill → agent follows SKILL.md instructions to self-route |
| **A: CLI** | Any framework with shell access | Call `skill-radar route "query"` before assembling prompt |
| **B: Python SDK** | Python-based agents, custom frameworks | `from skill_radar import load_skills` |
| **C: HTTP API** | Cloud agents, microservice architectures | `skill-radar serve --port 8900` |

### Mode D: Self-routing (zero integration effort)

Just install skill-radar as a skill in your agent. The SKILL.md contains instructions that tell the agent:

1. Run the routing script with the user's query
2. Read the JSON output
3. Load only the matched skills
4. Respond normally

No framework code changes needed. Works with any agent that can execute scripts.

### Mode B: Python SDK

```python
from skill_radar import load_skills

# Load all skills with routing declarations
router = load_skills("~/.workbuddy/skills/")

# Route a query
results = router.route("this SQL query is too slow, optimize it")
# → [ScoringResult(skill_name="sql-optimizer", score=0.39)]

# Use in your prompt assembly:
for r in results:
    print(f"Load skill: {r.skill_name} (score: {r.total_score})")
```

### Mode C: HTTP Server

```bash
skill-radar serve --skills-dir ./skills/ --port 8900
```

```bash
curl -X POST http://localhost:8900/route \
  -H "Content-Type: application/json" \
  -d '{"query": "production service returning 500 errors", "context": {"file_types": [".log"]}}'
```

---

## How Scoring Works

```
Score = 0.30 × keyword_ratio + 0.25 × pattern_hit + 0.15 × intent
      + 0.15 × context_bonus + 0.15 × priority/100 - anti_penalty
```

- **Keywords**: substring match, case-insensitive
- **Patterns**: regex match (supports Chinese + English)
- **Anti-patterns**: hard exclusion (score → 0)
- **Priority**: author-declared importance (0-100)
- **Context**: bonus for matching file types or workspace tags

Threshold strategies: `fixed` (score > 0.30), `top-k`, `gap-based`, `pattern-gate`.

---

## Routing Schema

Full schema documentation: [references/routing-schema.md](references/routing-schema.md)

```yaml
name: example-skill
description: "What this skill does"
routing:
  keywords: [...]        # Trigger words (substring match)
  patterns: [...]        # Regex patterns (precise triggers)
  intents: [...]         # Semantic intent tags
  anti_patterns: [...]   # Hard exclusion rules
  anti_keywords: [...]   # Soft penalty words
  priority: 50           # 0-100 importance weight
  mode: any              # any | all | threshold
  context:
    file_types: [...]
    workspace_hints: [...]
```

---

## Examples

The `examples/` directory contains 6 cross-domain skill routing configs:

- `contract-review` — Legal/compliance
- `code-review` — Software engineering
- `weather-query` — General utility
- `sql-optimizer` — Data engineering
- `ui-feedback` — Design
- `incident-triage` — SRE/DevOps

---

## When NOT to use Skill Radar

- **< 4 skills**: Just load them all, routing overhead isn't worth it
- **Highly ambiguous queries**: If users say things like "should I bring an umbrella tomorrow" (implying weather without saying "weather"), pure regex won't catch it — consider adding an embedding fallback
- **Rapidly changing skill set**: If skills are added/removed every minute, the init-time scanning may need to be event-driven

---

## Custom Integration Guide

If you're building your own agent framework and want to integrate skill-radar at a deeper level:

1. **Import the core engine** — `from skill_radar.core import SkillRouter` (zero I/O, pure computation)
2. **Register skills programmatically** — call `router.register_skill(RoutingConfig(...))` with your own data source
3. **Call `router.route(query)`** — get back scored results
4. **Use results to filter your prompt assembly** — only inject matched skill descriptions

The `core.py` module has NO file I/O, NO network calls, NO framework dependencies. It's a pure function: `(query, skills) → scores`.

---

## License

MIT

## Links

- GitHub: https://github.com/ninetyhe-90/skill-radar
- ClawHub: https://clawhub.ai/ninetyhe-90/skills/skill-radar
