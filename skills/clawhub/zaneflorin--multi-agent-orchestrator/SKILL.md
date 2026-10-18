---
name: "multi-agent-orchestrator"
description: "16 specialized agents with domain tools + 7 communication tools for coordinated multi-agent workflows. Implements Coordinator-Workers protocol."
---

# Multi-Agent Orchestrator Skill

**Triggers:** "spawn agent team", "multi-agent workflow", "coordinate specialists", "researcher coder writer reviewer", "parallel agent execution"

**Produces:** Configured multi-agent system with 16 specialized roles, domain toolsets, and 7 inter-agent communication primitives.

---

## Architecture Overview

16 specialized agents, each with:
- **Domain tools** (4–17 specific tools)
- **7 shared communication tools**: `consult_subagent`, `ask_subagent`, `post_to_blackboard`, `read_blackboard`, `send_agent_message`, `read_agent_inbox`, `broadcast_to_agents`

All agents inherit a persistent **Blackboard** for shared state, **P2P mailboxes** for direct messages, and **Broadcast** for team-wide notifications.

---

## Agent Registry

| Agent | Role | Domain Tools | Count |
|-------|------|--------------|-------|
| `analyze` | Analiză & Audit Date | read_file, list_directory, run_command, get_system_info, file_stats, parse_csv, parse_json, grep_file, count_lines | 9 |
| `research` | Cercetare Web | search_web, fetch_webpage, deep_research, extract_links | 4 |
| `coder` | Programare & Arhitectură | read_file, write_file, list_directory, run_command, run_code, run_python, check_python_syntax, grep_file, count_lines, file_stats | 10 |
| `writer` | Redactare & Conținut | read_file, write_file, list_directory, create_document, search_web, fetch_webpage, file_stats | 7 |
| `data` | Analiză Date & Vizualizări | read_file, write_file, parse_csv, parse_json, run_python, run_command, list_directory, file_stats | 8 |
| `security` | Audit Securitate & Privacy | read_file, list_directory, grep_file, file_stats, run_command, check_python_syntax | 6 |
| `planner` | Planificare & Strategie | read_file, list_directory, search_web, file_stats | 4 |
| `verify` | Verificare & Audit Livrabile | read_file, list_directory, run_command, search_web, check_python_syntax, file_stats, grep_file, count_lines | 8 |
| `repair` | Reparare & Depanare Erori | read_file, write_file, list_directory, run_command, run_code, move_or_copy, check_python_syntax, run_python | 8 |
| `devops` | DevOps & Automatizare Sistem | run_command, run_code, get_system_info, read_file, write_file, list_directory, file_stats, grep_file | 8 |
| `designer` | Frontend & Design UI/UX | read_file, write_file, list_directory, run_command, file_stats, grep_file | 6 |
| `translator` | Traducere & Localizare | read_file, write_file, create_document, search_web, fetch_webpage | 5 |
| `qa` | Testare & QA Automatizat | read_file, write_file, run_command, run_code, check_code_syntax, check_python_syntax, scan_codebase, search_code, list_directory, file_stats, grep_file, count_lines | 12 |
| `docs` | Documentare Tehnică & API Specs | read_file, write_file, create_document, read_document, list_directory, scan_codebase, search_code, grep_file, count_lines, file_stats, search_web, fetch_webpage | 12 |
| `git_refactor` | Git & Refactoring Arhitectural | git_status, git_log, git_diff, git_branch, run_command, read_file, write_file, scan_codebase, search_code, check_code_syntax, check_python_syntax, list_directory, file_stats, grep_file, github_list_repos, github_list_issues, move_or_copy | 17 |
| `scraper_api` | Web Scraping & Documentare API | scrape_page, fetch_webpage, search_web, rss_fetch, extract_entities, text_to_csv, extract_table_from_html, browser_open, browser_fetch, browser_screenshot, read_file, write_file, parse_json, parse_csv, run_command, run_code, list_directory | 17 |

---

## Communication Primitives (7 tools, available to ALL agents)

| Tool | Purpose |
|------|---------|
| `post_to_blackboard(key, value)` | Persistent shared key-value store |
| `read_blackboard(key)` | Read shared state |
| `send_agent_message(to_agent, message)` | Direct P2P message to agent inbox |
| `read_agent_inbox()` | Read own message queue |
| `broadcast_to_agents(message)` | Fan-out to all team members |
| `consult_subagent(agent, task)` | Synchronous sub-task delegation, returns result |
| `ask_subagent(agent, question)` | Async question, returns when answered |

---

## Coordination Protocol: Coordinator-Workers

**Pattern:** Coordinator decomposes task → spawns specialized workers → aggregates results → delivers final.

### Worker Contracts

**Researcher** — Input: `{ query, focus, output_format, limits }` → Output: structured brief + sources + uncertainty note

**Coder** — Input: `{ feature, context, requirements, tests, output_path }` → Output: code files + test results + docs

**Writer** — Input: `{ doc_type, sources, structure, tone, length }` → Output: polished document + references

**Reviewer** — Input: `{ artifact_path, audit_type, criteria, min_severity }` → Output: findings list + verdict (PASS/CONDITIONAL/FAIL) + blockers

### Spawning (via `sessions_spawn`)

```json
{
  "runtime": "subagent",
  "mode": "run",
  "agentId": "<agent-name>",
  "context": "isolated",
  "cleanup": "keep"
}
```

Each worker receives a structured task matching its contract. Results returned via completion path.

---

## Usage Patterns

### Pattern 1: Research → Code → Write → Review
```
Coordinator spawns: research → coder → writer → verify
Each passes artifact to next via blackboard/P2P
```

### Pattern 2: Parallel Fan-out
```
Coordinator broadcasts task → [analyze, security, qa] run in parallel
Results aggregated via blackboard
```

### Pattern 3: Iterative Refinement
```
Coordinator → coder (implement) → verify (audit) → repair (fix) → verify (re-audit)
```

---

## Quick Start (in a session)

1. **Spawn Coordinator** (this agent) with task
2. **Coordinator** decomposes, spawns workers via `sessions_spawn`
3. **Workers** execute with domain tools + communication tools
4. **Coordinator** aggregates, verifies, delivers

---

## Memory & Persistence

- **Blackboard**: Survives agent restarts, shared namespace
- **Agent Inboxes**: Per-agent message queues
- **Broadcast Log**: Append-only team notification history

---

## Verification Checklist

- [ ] All 16 agents spawn successfully
- [ ] Blackboard read/write works across agents
- [ ] P2P messages deliver to correct inbox
- [ ] Broadcast reaches all active agents
- [ ] consult_subagent returns structured result
- [ ] ask_subagent resolves async
- [ ] Coordinator-Workers contracts honored

---

## Related Skills

- `coordinator-workers-protocol` — core delegation pattern
- `clawhub` — for publishing/installing this skill

---

*Skill authored for OpenClaw Workshop. Apply to activate in this gateway.*
