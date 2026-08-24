# Secure Data Analyst Skill Suite

> **Version**: 1.2.0 · **Requires**: MGC Blackbox ≥ 1.4.10

A mixed-form skill suite combining **workflow prompts + an Agent system prompt template**, designed to help data analysts safely manage scripts, credentials, collaboration, and knowledge using **MGC Blackbox**.

---

## What This Skill Suite Provides

This suite enables data analysts to securely manage their end-to-end workflow **on their local machine**, including:

- **Credential management** — encrypted, zero-exposure storage
- **User-owned scripts** — safe application of query, cleaning, and analysis scripts
- **Script sealing & collaboration** — encrypted sharing across teams
- **Knowledge management** — store analysis frameworks and reusable prompts
- **Optional Agent template** — build a safe Data Analyst Agent that follows strict authorization rules

All sensitive operations require explicit user authorization.
This suite does **not** provide any automated data access capabilities.

---

## Prerequisites

- Python 3.10+
- Install MGC Blackbox:
  ```
  pip install mgc-blackbox
  ```
- Start MGC:
  ```
  mgc
  ```
  - WebUI: `http://127.0.0.1:57218` (Visual Interface)
  - API: `http://127.0.0.1:57219` (API Interface)
  - Token Required: Header "X-MGC-Token"
  - Token File: `~/.mgc/database/mgc_black_box/.mgc_token`

---

## Intended Users

- Data analysts working with sensitive business data
- Teams requiring secure script collaboration
- Organizations protecting local data assets
- Users building safe data-analysis Agents

---

## Secure Workflow Overview

```
┌──────────────────────────────────────────────┐
│           Secure Data Analysis              │
├──────────────────────────────────────────────┤
│                                              │
│  Credential → User Query Scripts → Cleaning │
│                                              │
│  → Analysis → Secure Delivery → Knowledge   │
│                                              │
└──────────────────────────────────────────────┘
```

All scripts are user-owned, all applications completed via MGC locally, AI cannot see scripts or credentials.

---

## Core Components

### 1. Credential Management

Users store database credentials in MGC for zero-exposure calling.

**Store credential:**
```
info_type: "credential"
info_owner: "db_connection_name"
content: Encrypted credential (user-owned)
```

**Call credential in scripts:** See `prompts/credential_management.md`

AI cannot see credentials.

---

### 2. Script Management

Users store query, cleaning, analysis scripts in MGC, apply after user authorization.

**Store script:**
```
info_type: "script"
info_owner: "script_name"
ext01: "python"
content: User-owned script
```

**Apply script:** See `prompts/script_management.md`

- Query scripts
- Cleaning scripts (pass previous result via ext02)
- Analysis scripts

---

### 3. Knowledge Management

Users store analysis frameworks, prompt templates, methodologies in MGC.

**Store knowledge:**
```python
mgc_save(
    info_type="prompt",
    info_owner="framework_monthly_sales",
    content="Analysis framework content"
)
```

See `prompts/knowledge_management.md`

---

## Security Boundaries (Must Follow)

### This Suite Provides:

- Local encrypted credential storage
- Zero-exposure application of user-owned scripts
- Script sealing & collaboration authorization
- Encrypted knowledge management

### This Suite Does NOT Provide:

- Automated data access
- Automated cleaning or analysis
- Automated transmission
- Cross-organization data transmission
- Script generation or modification

All scripts must be provided by the user and comply with organizational policies.

---

## Anti-Patterns & Pitfalls

### ❌ Common Mistakes

| Mistake | Risk | Correct Approach |
|---------|------|-----------------|
| Paste credentials in AI chat | Credential exposure | Store in MGC, call internally in scripts |
| Let AI auto-select script names | Script misuse risk | User must provide info_owner |
| Access credentials without authorization | Unauthorized access | Request user authorization before each access |
| Send script content to AI | Script exposure | Use MGC to apply, AI only sees results |
| Expect suite to auto-process data | Violates design | User-owned scripts, manually trigger each step |

---

## Complete Use Case

### Scenario: Monthly Sales Data Analysis

**Step 1: Preparation**

User stores credentials and scripts in MGC:
- Credential: `db_sales_prod`
- Query script: `query_monthly_orders`
- Cleaning script: `cleaning_standardize_date`
- Analysis script: `analysis_monthly_summary`

**Step 2: Workflow**

```
User: Help me analyze last month's sales data

Agent:
[1] Request authorization: Execute query script query_monthly_orders?
User: yes

[2] Execute query, return results

[3] Request authorization: Execute cleaning script cleaning_standardize_date?
User: yes

[4] Execute cleaning, pass previous result via ext02

[5] Request authorization: Execute analysis script analysis_monthly_summary?
User: yes

[6] Execute analysis, return report
```

Each step requires explicit user authorization. Agent cannot see script content or credentials.

---

## MCP Tools Reference

| Tool | Description |
|------|-------------|
| mgc_save | Store credentials, scripts, prompts |
| mgc_get | Apply scripts after user authorization |
| mgc_run | Execute a stored script (preferred over mgc_get action="run") |
| mgc_seal | Seal scripts for collaboration |
| mgc_list | List stored items (exact match) |
| mgc_find | Fuzzy-search entries by name (auto-applies LIKE wildcards; v1.4.10+) |
| mgc_open_webui | Open MGC WebUI |

---

## Prompt Templates (Skill Suite Section)

Located in `prompts/` directory:

- `credential_management.md` — Credential management workflow
- `script_management.md` — Script management workflow
- `knowledge_management.md` — Knowledge management workflow

---

## Agent Template (Hybrid Enhancement)

This skill suite includes an optional **Data Analyst Agent system prompt template**:

### agent_system_prompt.md

Used to build a safe data analysis Agent. The Agent will:

- Request user authorization before each sensitive operation
- Apply scripts via MGC after user authorization
- Must not view script content
- Must not access credentials
- Must not automatically execute workflows
- Must not auto-select script names (info_owner must be provided by user)

### How to Use Agent Template

1. When creating an Agent, use `agent_system_prompt.md` as the system prompt
2. Configure MCP tools: mgc_save / mgc_get / mgc_seal / mgc_list / mgc_open_webui
3. Agent can reference prompts in `prompts/` directory for workflow nodes

Agent is an optional enhancement, not a required component.

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Script application fails | Check if credentials stored correctly |
| Sealing fails | Ensure target node has MGC 1.4.6+ |
| Workflow interrupted | Check if user authorization is missing |

---

## Contact

- Issues: https://github.com/zkeviny/MGC-Blackbox/issues
- Email: mirgincipher@outlook.com

---

## License

MIT License

---

# Complete Note

This skill suite is for secure workflow management.
All sensitive operations require user authorization.
This suite does not provide any automated data access capabilities. All scripts must be provided by the user and comply with organizational policies.

---
