---
name: skill-manager
description: "Plugin & Skill management assistant: scans and analyzes all installed Plugins/Skills, evaluates functionality, features, dependencies, and potential risks, and recommends matching Skills based on current task complexity. Triggers: manage skills, analyze skills, skill management, plugin management, installed skills, skill analysis, skill recommendation, skill audit, skill inventory, skill matching, recommend skills, clean up skills."
---

# Skill Manager — Plugin & Skill Management Assistant

## Core Capabilities

1. **Skill Inventory Scan** — Automatically scans all installed Skills under `~/.qclaw/skills/`, extracting name, description, file structure, and script dependencies
2. **Deep Analysis** — Analyzes each Skill's functionality, platform origin, dependency chain, and potential risks
3. **Task Matching Evaluation** — Evaluates whether installed Skills match the current task complexity; searches external platforms for alternatives when no match is found
4. **Token Cost & Execution Time Estimation** — Compares "Use existing Skill" vs "Write new script" vs "Use built-in tools" in estimated token consumption and execution time
5. **Decision Routing** — Generates a report and lets the user manually choose an execution path; never auto-executes

## Workflow

### Phase 1: Scan Installed Skills

Run the scan script to get a complete inventory:

```bash
python3 scripts/scan_skills.py --path ~/.qclaw/skills --output json
```

The script outputs a JSON array where each element contains:
- `name`: Skill name
- `description`: Description from frontmatter metadata
- `dir_size`: Directory size (KB)
- `file_count`: Number of files
- `has_scripts`: Whether executable scripts are included
- `has_references`: Whether reference docs are included
- `has_assets`: Whether asset files are included
- `scripts_list`: List of script files
- `dependencies`: External tools/runtimes depended on
- `risk_level`: Risk level (low/medium/high)
- `risk_notes`: Risk explanation

### Phase 2: Task Complexity Assessment

Evaluates task complexity based on the user's current request, classified into three levels:

| Level | Definition | Strategy |
|-------|-----------|----------|
| **Simple** | Single-step operation, simple query, one-time conversion, short text processing | Prefer built-in tools for direct execution, no skill recommendation needed |
| **Medium** | Multi-step workflow, requires domain-specific knowledge, involves external APIs | Evaluate installed skill match, compare three paths (existing skill / built-in tools / write script) by token cost, recommend optimal |
| **Complex** | Multi-domain crossover, long workflow, requires professional toolchain, recurring pattern | Search major platforms for recommended skills, compare three paths by token cost, provide installation suggestions |

Complexity assessment dimensions:
- Number of steps (1 step = simple, 2-3 steps = medium, 4+ steps = complex)
- Whether domain-specific knowledge is needed
- Whether external APIs or specific runtimes are needed
- Whether it's a recurring task (repeated use → lean toward recommending a Skill)
- Estimated code volume (<50 lines = simple, 50-200 lines = medium, >200 lines = complex)

### Phase 3: Matching Analysis & Recommendations

#### 3a. Installed Skill Matching

Evaluates each installed skill's match level for the current task:

- **High match**: Skill description directly covers task requirements → Use directly
- **Partial match**: Skill covers part of the requirements → Use + supplement
- **No match**: No relevant skills → Enter recommendation flow

#### 3b. External Search Recommendations (Complex tasks only)

When the task is complex and no installed skill matches, search these platforms:

1. **SkillHub** — Online repository via `skillhub_install` tool
2. **skills.sh** — `npx skills find <query>` search
3. **GitHub** — `web_search` for "openclaw skill <keyword>" or "claude skill <keyword>"
4. **npm** — Search for relevant MCP servers or CLI tools

After searching, compile a recommendation list including:
- Skill name and source
- Function summary
- Installation command
- Estimated token savings
- Risk assessment

#### 3c. Token Cost & Execution Time Comparison

For each recommended option, estimate token consumption and execution time across three paths:

| Path | Token Estimate | Time Estimate |
|------|---------------|---------------|
| **Use existing Skill** | SKILL.md loading (~500-2000 tokens) + script execution (~200-1000 tokens) | Loading ≈10s + ~5s per step |
| **Use built-in tools** | Tool call overhead (~200 tokens) + result parsing (steps×150) + retries (steps×100) | Direct call ≈3s + ~4s per step |
| **Write new script** | Requirements analysis + code generation + debugging + error handling, typically 3000-15000 tokens | Analysis+generation ≈20s + 0.5s per code line + 5s debugging per step |

Formulas:
- Existing skill cost ≈ `skill_md_tokens (typically 500-2000)` + `call_tokens (typically 200-1000)`
- Existing skill time ≈ `10s (loading)` + `steps × 5s`
- Built-in tools cost ≈ `tool_call ≈200` + `result_parsing ≈ steps×150` + `retry_reserve ≈ steps×100`
- Built-in tools time ≈ `3s (first call)` + `steps × 4s`
- Write script cost ≈ `code_lines × 15 tokens/line` + `debug_tokens (~30% of code)`
- Write script time ≈ `20s (analysis+generation)` + `code_lines × 0.5s` + `steps × 5s`

**Decision principle:** Always present both Token and time dimensions for comparison. Let the user choose based on their needs. Never auto-execute. The token-optimal and time-optimal paths may differ.

### Phase 4: Report Output

Generates a structured report in the following format:

```markdown
# 📋 Skill Management Report

## Current Task Analysis
- **Task**: [description]
- **Complexity**: [Simple/Medium/Complex]
- **Basis**: [reasoning]

## Installed Skills Overview (N total)
| Skill | Function | Risk | Match |
|-------|----------|------|-------|
| ... | ... | ... | ... |

## Match Evaluation
- **Matched skills**: [name] — Use directly
- **Partial match**: [name] — [notes]
- **Missing capabilities**: [description]

## Recommendations (Complex tasks only)
### Recommendation 1: [skill name]
- **Source**: [platform]
- **Function**: [description]
- **Install**: `command`
- **Token comparison**: Install ≈X tokens vs Write ≈Y tokens
- **Risk**: [assessment]

## Decision Suggestion
[Direct execution / Recommend install / User choice]
```

### Phase 5: User Selection (No Auto-Execution)

**Core principle: After generating the report, the user must manually select an execution path. Never auto-execute any recommendation.**

After generating the report, use `render_ui` with `QuestionForm` to present options to the user:

- List available paths based on the Token + time comparison in the report (2-4 options)
- Each option shows estimated Token consumption and execution time
- Include a "Write new script" option
- Execute the chosen path only after user confirmation
- If the user doesn't select, do not auto-execute any path

Example options:
- "Use built-in tools (~700 tokens, ~7s, Token+time optimal)"
- "Use existing skill xxx (~1980 tokens, ~20s)"
- "Write new script (~1521 tokens, ~55s)"
- User can also enter a custom option

**Simple tasks are also not auto-executed** — a report is still generated and the user must confirm.

## Risk Assessment Framework

Each installed or recommended skill is assessed across these dimensions:

| Dimension | Low | Medium | High |
|-----------|-----|--------|------|
| **Data access** | Local files only | Reads external APIs | Writes to external systems / sends data |
| **Permissions** | No extra permissions | Requires API Key | Requires OAuth / admin privileges |
| **Network dependency** | Purely local | Requires network queries | Strongly depends on external service availability |
| **Code source** | Official / verified | Community-maintained | Unknown source / unverified |
| **Destructive operations** | Read-only | Can modify local files | Can delete / send / publish |

Overall risk = highest risk dimension level.

## Usage Examples

### Example 1: Simple Task — User selects after report
> User: "Convert this CSV to JSON"
>
> Assessment: Simple task (1 step, purely local, <50 lines of code)
> Token + time comparison: Built-in ≈350 tokens/~7s vs Existing skill ≈1580 tokens/~15s vs Write script ≈1250 tokens/~35s
> Action: Generate report, present options for user to choose, do not auto-execute

### Example 2: Medium Task — Compare three paths, user selects
> User: "Generate a map webpage with several store locations marked"
>
> Assessment: Medium task (multi-step, requires map API knowledge)
> Token + time comparison: Existing skill tencentmap-jsapi-gl-skill ≈1980 tokens/~20s vs Built-in ≈750 tokens/~11s vs Write script ≈2799 tokens/~75s
> Action: Generate report, present three paths for user to choose, do not auto-execute

### Example 3: Medium Task, No Match — User selects
> User: "Scrape task and creator info from this website"
>
> Assessment: Medium task (requires network requests + data parsing)
> Token + time comparison: Built-in ≈900 tokens/~11s vs Write script ≈2799 tokens/~75s
> Action: Generate report, present options for user to choose, do not auto-execute

### Example 4: Complex Task — Search recommendations, user selects
> User: "Build a complete automated data pipeline — extract, transform, load into data warehouse"
>
> Assessment: Complex task (multi-domain, long workflow, requires professional toolchain)
> Token + time comparison: Built-in ≈1050 tokens/~19s vs Write script ≈6414 tokens/~180s (no matching skill)
> Action:
> 1. Scan installed skills → Find no match
> 2. Search external platforms → Find relevant Skills
> 3. Present three-path comparison → User selects → Do not auto-execute

## Notes

- Scan results should be cached to avoid repeated scanning (unless the user requests a refresh)
- Prioritize officially verified skill sources in recommendations
- Risk assessments should be honest and transparent — never hide potential issues
- Token and time estimates are rough references; actual consumption varies by model and implementation
- For tasks involving sensitive data, additionally check the skill's data handling practices before recommending
