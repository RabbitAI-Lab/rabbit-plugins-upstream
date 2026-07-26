---
name: alazab-global-context
description: Shared production context, operational paths, orchestration policies, agent routing, approvals, deployment and execution standards for all Alazab Portal AI agents, models, sessions and nodes.
version: 1.0.0
author: alazabdev
homepage: https://clawhub.ai/alazabdev
metadata:
  scope: global
  environment: production
  auto_attach: true
  context_file: alazab-portal-ai-global-context.json
---

# Alazab Portal AI — Global Skills

## Purpose

This file defines the shared operational skills loaded by default for all agents, models, runtimes, sessions, projects, and execution nodes in the Alazab AI Portal.

Canonical global context:

```text
/etc/portal-ai/shared/alazab-portal-ai-global-context.json
```

The same file must be used by both production servers:

```text
portal-ai.alazab.com
portal-ai.alazab.cloud
```

## Scope

```yaml
scope: global
auto_attach: true
applies_to:
  agents: ["*"]
  models: ["*"]
  runtimes: ["*"]
  sessions: ["*"]
  projects: ["*"]
  nodes: ["*"]
```

## Context Loading Order

Every agent or model must load context in this order:

1. Global context
2. Organization policies
3. Project context
4. Agent role
5. Mission context
6. Task context
7. Current user instruction

Later layers may override earlier layers only within their permitted scope.

## Global Skills

### 1. Mission Planning

Convert a user request into:

- Mission
- Workstreams
- Tasks
- Dependencies
- Risks
- Acceptance criteria
- Rollback plan

No execution starts before the target environment, node, paths, and success criteria are known.

### 2. Agent Routing

Select the correct agent, model, or runtime based on:

- Task domain
- Required tools
- Target node
- Data sensitivity
- Cost
- Latency
- Context-window requirements
- Review requirements

Supported execution targets include:

- Codex CLI
- Gemini
- Azure AI Foundry agents
- Azure-hosted models
- Ollama models
- PTY shell executor
- Specialized review agents

### 3. Multi-Agent Orchestration

Support:

- Sequential execution
- Parallel execution
- Supervisor-worker execution
- Independent review
- Retry and recovery
- Escalation to owner approval
- Consolidation of outputs

Agents must not duplicate work unless parallel comparison is explicitly requested.

### 4. Project Context Management

Every active project should maintain:

```text
PROJECT.md
ARCHITECTURE.md
DECISIONS.md
CURRENT_STATE.md
KNOWN_ISSUES.md
SERVICE_MAP.md
EXECUTION_PLAN.md
TASKS/
REPORTS/
RUNS/
ARTIFACTS/
BACKUPS/
```

Agents must update project state after material changes.

### 5. Production Path Awareness

#### Core server

```text
/var/www/core/portal-ai
/etc/portal-ai/core
/var/lib/portal-ai/core
/var/log/portal-ai/core
/var/backups/portal-ai/core
```

#### Cloud server

```text
/var/www/apps/portal-ai
/etc/portal-ai/cloud
/var/lib/portal-ai/cloud
/var/log/portal-ai/cloud
/var/backups/portal-ai/cloud
```

#### Shared paths

```text
/etc/portal-ai/shared
/etc/portal-ai/shared/skills
/etc/portal-ai/shared/policies
/etc/portal-ai/shared/schemas
/etc/portal-ai/shared/templates
```

Agents must never invent production paths when the global context already defines them.

### 6. Safe Production Execution

Before changing production systems:

1. Inspect current state.
2. Identify affected services and files.
3. Create backup or snapshot.
4. Record rollback procedure.
5. Apply the smallest valid change.
6. Run validation tests.
7. Verify service health.
8. Record the result.

Non-destructive, reversible operations may proceed automatically.

Destructive or irreversible operations require explicit owner approval.

### 7. Approval Control

Approval is required for operations including:

```text
DROP DATABASE
DROP SCHEMA
rm -rf
pg_dropcluster
initdb on existing data
pg_resetwal
force push
DNS deletion
firewall flush
secret rotation
```

Approval requests must state:

- Exact command
- Target node
- Affected resources
- Expected impact
- Backup status
- Rollback procedure

### 8. Evidence-Based Diagnosis

Agents must:

- Inspect before modifying.
- Use logs, configuration, process state, and service state as evidence.
- Avoid assumptions.
- Stop when evidence indicates corruption or an unsafe state.
- Distinguish temporary runtime files from critical data or catalog files.

### 9. API and Integration Design

All Core-to-Cloud communication must use authenticated internal APIs over the private network.

Default internal endpoints:

```text
Core:  http://10.77.0.1:8200
Cloud: http://10.77.0.2:8100
```

Required request identity:

```text
Authorization: Bearer <service-token>
X-Alazab-Node: <node-id>
X-Alazab-Timestamp: <timestamp>
X-Alazab-Signature: <hmac-signature>
```

Execution nodes must not write directly to the Core database.

### 10. Codex Session Management

Codex execution must support:

- Session creation
- Task submission
- Follow-up messages
- Transcript retrieval
- Interrupt
- Resume
- Timeout handling
- Exit-code capture
- Artifact collection
- Independent review

Default Codex paths:

```text
/var/lib/portal-ai/cloud/workspaces/codex
/var/lib/portal-ai/cloud/sessions/codex
/var/log/portal-ai/cloud/codex
```

### 11. Model Selection

Use the smallest model that can complete the task reliably.

Recommended routing:

- Architecture and orchestration: `az-model-core`
- Maintenance operations: `az-model-maint`
- Financial analysis: `az-model-finance`
- Embeddings and semantic retrieval: `az-models-text`
- Speech-to-text: `az-modelspeech`
- Voice interaction: `az-model-voice`
- Local coding: `deepseek-coder-v2:16b`
- Local vision: `llama3.2-vision:11b`
- Local OCR: `deepseek-ocr:latest`

### 12. Quality Review

No task is complete until the result is checked against:

- User request
- Acceptance criteria
- Current architecture
- Security boundaries
- Production paths
- Test results
- Rollback readiness

High-impact tasks require independent review by a different agent or model.

### 13. Logging and Audit

Every execution event should include:

```text
timestamp
node_id
project_id
mission_id
task_id
agent_id
session_id
event_type
status
message
```

Logs must be structured as JSONL where supported.

### 14. Error Handling

When an operation fails:

1. Stop dependent steps.
2. Preserve logs and outputs.
3. Capture exit code.
4. Determine whether rollback is needed.
5. Do not conceal partial failure.
6. Report the exact failing component.
7. Resume only from a verified safe state.

### 15. Secret Handling

Secrets must be resolved from Infisical at runtime.

Production secret manager:

```text
https://env.alazab.com
```

Rules:

- Never write secrets into this file.
- Never commit secrets.
- Refer to secrets by environment-variable name.
- Redact credentials from logs and reports.

### 16. Deployment

Production deployment uses release directories and an atomic `current` symlink.

Core:

```text
/var/www/core/portal-ai/releases/<release-id>
/var/www/core/portal-ai/current
```

Cloud:

```text
/var/www/apps/portal-ai/releases/<release-id>
/var/www/apps/portal-ai/current
```

Required deployment checks:

- Configuration validation
- Backup
- Dependency lock verification
- Tests
- Security audit
- Health check
- API contract check
- Worker heartbeat
- Smoke test

### 17. Rollback

Application rollback:

```text
Switch current symlink to the previous verified release.
Restart affected services.
Run health and smoke tests.
```

Database rollback must use an approved recovery plan and a verified backup.

### 18. Communication Standard

Agent responses must be:

- Direct
- Evidence-based
- Actionable
- Specific to the current request
- Free of invented details

Operational reports must clearly separate:

- Confirmed state
- Changes made
- Validation results
- Remaining risks
- Next required action

## Mandatory Runtime Variables

```text
PORTAL_AI_NODE_ID
PORTAL_AI_NODE_ROLE
PORTAL_AI_ENVIRONMENT
PORTAL_AI_GLOBAL_CONTEXT
PORTAL_AI_SERVICE_TOKEN
PORTAL_AI_HMAC_SECRET
PORTAL_AI_DATABASE_URL
PORTAL_AI_REDIS_URL
PORTAL_AI_INFISICAL_PROJECT
```

## Canonical Skill Installation Path

```text
/etc/portal-ai/shared/skills/alazab-global-context/SKILLS.md
```

Repository development path:

```text
skills/alazab-global-context/SKILLS.md
```

## Final Rule

The global context file is the source of truth for infrastructure, paths, nodes, services, agents, models, and production rules.

This skills file defines how every agent and model must use that context during planning, execution, review, and reporting.
