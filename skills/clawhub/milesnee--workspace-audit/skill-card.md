## Description: <br>
Software-engineering system audit for Agent workspaces that uses DDIA reliability and DDD bounded-context analysis to diagnose schema drift, consistency gaps, query degradation, lifecycle bloat, and architectural coupling during periodic health checks or stale, bloated, inconsistent workspace conditions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[milesnee](https://clawhub.ai/user/milesnee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent-ops maintainers use this skill to audit OpenClaw-style workspaces and Hermes agent environments for memory drift, schema gaps, query degradation, lifecycle bloat, and architectural coupling. It helps produce baseline metrics, prioritized findings, validation results, and remediation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can direct agents to modify or delete local workspace and Hermes agent data without consistently requiring user approval. <br>
Mitigation: Require explicit approval before any move, rewrite, cron change, config change, database maintenance, archive compression with source removal, log deletion, session deletion, or other destructive workspace maintenance. <br>
Risk: The Hermes procedure touches high-impact local agent state, including memory, session history, cron delivery state, and security-sensitive configuration. <br>
Mitigation: Run read-only baseline and diagnosis steps first, confirm the target scope, preserve backups where available, and review each proposed Hermes change before execution. <br>


## Reference(s): <br>
- [Audit Checklist](references/audit-checklist.md) <br>
- [DDIA + DDD Memory System Mapping](references/ddia-ddd-mapping.md) <br>
- [Hermes Agent System Audit Procedure](references/hermes-audit-procedure.md) <br>
- [OpenClaw Workspace Audit 2026-07 Execution Log](references/openclaw-workspace-audit-2026-07.md) <br>
- [Audit Report Template](assets/audit-report-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, JSON baselines, shell commands, and code/configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces audit findings and proposed remediation steps; executing fixes may modify local workspace data.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
