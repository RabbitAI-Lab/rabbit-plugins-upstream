---
name: competitive-agent-loop
description: "3-Agent competitive loop with Planner/Generator/Evaluator and Sprint Contract"
author: wljmmx
version: 1.0.0
---

# Competitive Agent Loop Skill

## Overview
Standardized workflow based on Anthropic 3-Agent architecture.
Implements Planner/Generator/Evaluator role separation with multi-solution competition and Sprint Contract mechanism.

**Core thesis:** "The winners will not have the smartest model, they will have the best loop."

## Trigger Conditions
When receiving a development task, auto-determine complexity level:
- **Simple (<3 acceptance criteria)** - Single solution serial execution
- **Medium (3-8 criteria)** - Dual-solution time-sliced competition
- **Complex (>8 criteria or user demands quality-first)** - Multi-solution evaluation + strict verification

## Agent Role Mapping

| Agent | Role | Responsibility | Model | VRAM |
|-------|------|----------------|-------|------|
| main | Planner | Requirements analysis, complexity assessment, orchestration | qwen3.6_35b_un | ~20GB |
| coder | Generator | Code implementation, contract-based delivery | qwen3.6_35b_un | ~20GB |
| checker | Evaluator | Independent verification, scoring, acceptance reports | Qwythos | ~6GB |
| memowriter | Documenter | Documentation, technical reports, knowledge base | qwen3.5:9b | ~6GB |

VRAM constraint: RTX 4090 (24GB), coder (~20GB) and checker (~6GB) execute serially, peak ~20GB. keep_alive=1h keeps models warm; serial execution avoids VRAM contention.

## Workflow

### Phase A: Sprint Contract Negotiation
1. main analyzes requirements, generates initial acceptance criteria draft
2. spawn coder to propose implementation plan and acceptance criteria, push completion yields contract.json
3. spawn checker to review if criteria are verifiable or too loose/strict, push completion yields approved/revised status
4. **Human approval gate**: show final contract, wait for user confirmation

### Phase B: Multi-Solution Competition (Dynamic Time Allocation by Complexity)
main assesses complexity of each approach and calculates time budget

Formula:
dev_time = accepted_standards x base_time(3min) x complexity_multiplier
verify_time = dev_time x 0.4
total_budget = dev_time + verify_time

Per solution execution flow:
1. spawn coder to implement Solution X per contract (development time: dev_time min)
2. push completion yields code_output
3. spawn checker to verify each criterion and score (verification time: verify_time min)
4. push completion yields score, passed list, failed list, critique

Execution order: simple solutions first for quick baseline, complex solutions follow

### Phase C: Comparison and Selection plus Iteration Control
1. main compares scores across solutions, selects winner
2. **Human confirmation of final selection required**
3. Iterate on winning solution, max iterations cycles allowed
4. All verifications passed triggers spawn memowriter for documentation

## Complexity Assessment Template

| Factor | Weight | Description |
|--------|--------|-------------|
| new_technology_learning | 0.3 | New tech learning cost (0-1) |
| integration_complexity | 0.25 | Integration complexity (0-1) |
| data_model_changes | 0.2 | Data model change volume (0-1) |
| test_coverage_needed | 0.15 | Test coverage scope (0-1) |
| deployment_risk | 0.1 | Deployment risk (0-1) |

complexity_multiplier = sum(factors)
Examples: simple=1.2, medium=2.5, complex>3.0

## Human Intervention Points

| Point | Trigger Condition | Decision |
|-------|-------------------|----------|
| Contract Approval | After coder+checker negotiation complete | Are criteria reasonable? Is tech approach acceptable? |
| Consecutive Failure Threshold | 3 failed iterations in same sprint | Direction adjustment/solution swap/terminate sprint |
| Fallback Switch | Fallback triggered | Specific decisions on changing tech route |
| Final Sign-off | All verifications passed | Last quality gate before delivery |

## Iteration Control Hard Limits
- max_iterations_per_sprint: 5
- accept_rate_threshold: 0.3 (human intervention if pass rate < 30%)
- consecutive_failures[2]: Notify user, suggest contract adjustment
- consecutive_failures[3]: Provide alternative solutions for selection
- consecutive_failures[5]: Terminate sprint, request human takeover

## Required Output Formats

### coder must produce:
- summary: Implementation overview (max 100 chars)
- changes_made: Specific modifications (file + line ranges)
- acceptance_proof:
  - command_success: Verification command + expected output
  - response_check: Test endpoint + expected status code + content match
- known_issues: Known unresolved problems

### checker must produce:
- score: 0-10 rating
- passed_criteria: [list of passed criterion IDs]
- failed_criteria: [list of failed criterion IDs]
- critique:
  - severity: high/medium/low
  - criterion_id: Corresponding criterion ID
  - description: Specific issue description
  - fix_suggestion: Fix recommendation (with file path and line numbers)
- overall_verdict: pass/fail/review_needed

### memowriter must produce:
- sprint_summary: What was accomplished in this sprint
- decisions_made: Key technical decisions and rationale
- problems_encountered: Issues met and solutions found
- lessons_learned: Experiences captured for future reference
- deliverables: README/CHANGELOG/API docs/deployment guide

## OpenClaw Native Mechanisms Used

| Mechanism | Purpose |
|-----------|---------|
| Task Flow managed mode | Persistent workflow orchestration, survives restarts |
| sessions_spawn | Agent parallel scheduling with agentId targeting |
| push completion | Post-task push notification, no polling needed |
| SQLite durable state | Progress persistence + revision tracking |
| notification policy | done_only (terminal state notifications only) |

## Important Notes
1. Serial execution - Limited GPU, coder/checker must queue serially
2. Time control - timeoutMs = time_budget x 60000 x 1.5 (50% buffer)
3. Workspace sharing - Isolate changes via git commits
4. No polling - Rely on push notification mechanism
5. Human intervention timing - Only pause at critical decision points, auto-iterate normally

## Agent Model Fallback Chain

Each agent has a fallback chain for resilience if the primary model is unavailable.

| Agent | Primary | Fallback 1 | Fallback 2 |
|-------|---------|-----------|-----------|
| main (Planner) | qwen3.6_35b_un | qwen3.6:27b | Qwythos |
| coder (Generator) | qwen3.6_35b_un | qwen3.6:27b | Qwythos |
| checker (Evaluator) | Qwythos | qwen3.6_35b_un | qwen3.6:27b |
| memowriter (Documenter) | qwen3.5:9b | Qwythos | qwen3.5:4b |

### Fallback Priority Rules
1. Primary model is preferred; only fall back if unavailable or OOM
2. coder is the most frequently called agent; 35b_un (167 tok/s) replaced 27b (45 tok/s) as primary for 3.7x speed gain with equal code quality (60/60 vs 58/60)
3. Qwythos (108 tok/s, 38K output) serves as the long-output escalation option for any agent when deep analysis or extensive reports are needed
4. Excluded models (tested and rejected): qwq-unsloth (num_ctx 128K unsupported), gemma4:31b (timeout >600s), gemma4:26b (25 tok/s), qwen3-coder (23 tok/s, 175s load), qwen3.5:9b (275/360 quality, frontend=0/20)

### Session Model Priority (Runtime Optimization)

When the current conversation session uses a **local Ollama model** (provider is “ollama” or “ollama-256k”), all child agents should prefer using the **same model as the session’s primary model** to avoid repeated model loading/unloading on the GPU.

**Rule:**
- If session main model is an Ollama local model (provider = ollama/ollama-256k) → use session model for ALL child agents
- If session main model is a non-local model (e.g., deepseek, openai, anthropic) → use the configured model assignments as defined above

**Rationale:**
When coder/session models differ (e.g., session uses qwen3.6_35b_un while coder is configured for qwen3.6:27b), each agent switch forces Ollama to unload the current model and load another, causing 100s+ of latency per swap. For RTX 4090 with 24GB VRAM, even with keep_alive=1h, the GPU can only hold one large model at a time. Using the session model exclusively avoids this thrashing entirely.

**When session model is local Ollama, effective runtime assignment:**
| Agent | Model |
|-------|-------|
| main | session model |
| coder | session model |
| checker | session model |
| memowriter | session model |

**Note:** For cloud/hosted models (non-Ollama), the original tiered model assignments still apply as hardware limits are not a concern.

## Model Selection Rationale

Why each agent uses its assigned model:

### main → qwen3.6_35b_un (35B MoE, ~20GB)
Global brain requiring maximum reasoning depth for requirement decomposition, complexity assessment, and solution comparison. No-audit version enables unrestricted judgment. Serial execution means VRAM swap cost is negligible.

### coder → qwen3.6_35b_un (35B MoE, ~20GB)
Code generation is the most frequently called agent per sprint. Benchmarks show 35b_un and 27b have nearly identical code quality (60/60 vs 58/60 coding, both 60/60 fullstack), but 35b_un is 3.7x faster (167 vs 45 tok/s). This speed advantage means faster iteration cycles and shorter sprint times, directly impacting user experience. coder workload (~20GB) and checker (~6GB) execute serially within the 24GB RTX 4090 limit.

### checker → Qwythos (9B, ~6GB)
Pure evaluation task (score assignment, criteria verification, fix suggestions). 9B inference capability is sufficient for checklist-style validation. Chain-of-thought depth of 32B models provides diminishing returns here. Main already analyzed requirements upfront; checker executes acceptance checks.

### memowriter → qwen3.5:9b (9B, ~6GB)
Documentation generation requires sufficient output capacity for technical reports. Benchmarks show 9b scores 60/60 on document tasks versus 4b only generating 2.4K tokens before stopping. At 115 tok/s, 9b is fast enough for non-blocking documentation work, and its 6GB VRAM fits easily within the 24GB limit alongside serial execution with coder and checker.
