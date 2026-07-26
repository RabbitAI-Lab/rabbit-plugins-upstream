---
name: skill-builder
description: |
  Create a new OpenClaw skill with a short eval-driven loop.
  Activate when user asks to create a skill, turn a repeated workflow into a skill,
  or build a new reusable procedure.
---

# Skill Builder — Create Reusable Skills

This skill guides you through creating a new OpenClaw skill from a repeated workflow.

## When to Use

- User asks to "create a skill", "make this a skill"
- You notice the same workflow runs 3+ times → suggest making it a skill
- User wants to automate a repeated procedure
- Building a new reusable tool for a specific domain

**Not for:** Improving existing skills (use `skill-refiner` instead).

## The Skill Creation Loop

```
Observe pattern → Define skill → Write SKILL.md → Test → Refine
```

### Phase 1: Observe & Define

Before writing anything, understand:
1. **What triggers this skill?** (keywords, context, user request pattern)
2. **What does it do?** (the workflow, step by step)
3. **What are the inputs?** (what does the user need to provide)
4. **What are the outputs?** (what does the user get back)
5. **What could go wrong?** (edge cases, failure modes)

### Phase 2: Write the SKILL.md

Every skill has a header + body:

```markdown
---
name: <skill-name>
description: |
  One-line description. Activate when user mentions [trigger keywords].
---

# <Skill Name>

[Detailed description of what this skill does]

## When to Use
[When to activate this skill]

## How to Use
[Step-by-step workflow]

## Inputs
- `[param]`: [description]

## Outputs
[What the skill produces]

## Examples
```
[example usage with inputs/outputs]
```

## Edge Cases
- [case 1]: [how to handle]
- [case 2]: [how to handle]

## Notes
[Any caveats or special considerations]
```

### Phase 3: Test

Run the skill with real inputs:
1. Test with typical case
2. Test with edge cases
3. Fix issues found

### Phase 4: Refine

Based on test results:
- Simplify if too complex
- Add missing cases
- Clarify ambiguous instructions
- Reduce token cost if possible

## Skill Naming

- Use `kebab-case`: `feishu-doc`, `deep-research`, `skill-builder`
- Make the name self-explanatory: `code-reviewer` vs `cr-skill`
- Match trigger keywords in description

## Skill Locations

| Location | When to Use |
|----------|-------------|
| `workspace/skills/<name>/SKILL.md` | Workspace-specific, one-off skills |
| `~/.openclaw/skills/` | Personal reusable skills |
| Bundled with plugins | Skills that ship with installed plugins |

## Quality Checklist

- [ ] Name is clear and self-explanatory
- [ ] Description mentions trigger keywords
- [ ] Step-by-step workflow is clear
- [ ] All inputs/outputs documented
- [ ] Edge cases covered
- [ ] Examples included
- [ ] Token cost reasonable (avoid bloat)
- [ ] No secrets or credentials hardcoded
- [ ] Language matches user expectations (中文/English)

## Common Mistakes

### Too Generic
❌ "This skill helps with tasks"
✅ "Schedule reminders with natural language: 'remind me tomorrow at 9 to call Mom'"

### Too Long
❌ 50 steps for a simple workflow
✅ Break into sub-skills or simplify

### Missing Edge Cases
❌ "Read the file" (what if it doesn't exist?)
✅ "Read the file — if it doesn't exist, return 'File not found: [path]'"

### No Examples
❌ "Use the tool"
✅ "Use the tool: `feishu_doc(action='read', doc_token='ABC123')` → returns {title, content, ...}"

## From Workflow to Skill: Example

### Observed Pattern
User repeatedly asks: "check if server X is up" and you run:
1. SSH to server
2. Check systemctl status
3. Check recent logs
4. Return status summary

### Skill Definition
```markdown
---
name: server-health-check
description: |
  Check server health status via SSH. Activate when user mentions
  checking a server, server status, or "is X up".
---

# Server Health Check

Quick health check for a server via SSH.

## How to Use

1. **Identify server** — which server to check? (hostname or IP)
2. **SSH connect** — connect to server (check ~/.ssh/config for host details)
3. **Run health checks:**
   - `systemctl status <service>` — is the service running?
   - `journalctl -n 20 --no-pager` — recent logs
   - `df -h` — disk space
   - `free -h` — memory
4. **Summarize** — return a concise status report

## Inputs
- `server`: hostname or IP address

## Outputs
```
Server: [server]
Status: [running/down/degraded]
Services: [list running services]
Disk: [usage%]
Memory: [usage%]
Recent Alerts: [any errors in logs]
```

## Edge Cases
- **Connection refused:** Return "Cannot connect to [server]. Check if server is running or SSH is accessible."
- **Service not found:** Note it in output, don't fail
- **Partial failure:** Report what succeeded, flag what failed

## Notes
- Use `paramiko` on Windows, `ssh` on Linux/Mac
- SSH credentials should be in `~/.ssh/config`, not hardcoded
```

---

## Skill Lifecycle

1. **Create** — write initial SKILL.md
2. **Test** — run with real inputs
3. **Deploy** — save to appropriate location
4. **Use** — activated by trigger keywords
5. **Refine** — improve based on usage feedback
6. **Deprecate** — when no longer needed, disable in config

## Notes

- Skills are hints, not guarantees — always verify before acting on memory
- Code identifiers and paths stay in native form regardless of surrounding language
- Write skill entries in the user's language (中文/English)
- If user language is mixed, keep natural language entries consistent with surrounding content