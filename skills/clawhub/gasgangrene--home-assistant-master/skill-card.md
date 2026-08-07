## Description: <br>
Home Assistant OS (HAOS) operations skill for OpenClaw agents that supports read-only audits, diagnostics, automation design and review, dashboard planning, integration risk assessment, backup readiness checks, and safety-gated maintenance playbooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gasgangrene](https://clawhub.ai/user/gasgangrene) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to troubleshoot Home Assistant entities, devices, integrations, automations, dashboards, and backup readiness while keeping operational changes approval-gated. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Operational access to a Home Assistant instance can affect devices, automations, and security-sensitive controls if writes are approved too broadly. <br>
Mitigation: Install only in a private, trusted agent environment, start in read-only mode, preview exact impact, and require explicit scoped confirmation with two-step confirmation for sensitive or platform-level actions. <br>
Risk: Credentials or tokens could be exposed if users paste long-lived secrets into chat or store them in skill files. <br>
Mitigation: Use platform-managed secret storage or least-privilege tokens, avoid requesting long-lived secrets in public or group chats, and redact sensitive values in outputs. <br>
Risk: Incorrect diagnostics or automation guidance could reduce reliability or create unsafe Home Assistant behavior. <br>
Mitigation: Collect traces, history, logs, and integration state before recommending changes, prefer official Home Assistant documentation when guidance conflicts, and verify outcomes after approved changes. <br>


## Reference(s): <br>
- [Safety Policy](references/safety-policy.md) <br>
- [Standard Workflows](references/workflows.md) <br>
- [Access & Credentials Requirements](references/access-and-credentials.md) <br>
- [Canonical Citations](references/citations.md) <br>
- [Home Assistant Documentation](https://www.home-assistant.io/docs/) <br>
- [Home Assistant Automation Documentation](https://www.home-assistant.io/docs/automation/) <br>
- [Home Assistant Security Documentation](https://www.home-assistant.io/docs/configuration/securing/) <br>
- [Home Assistant OS Backups](https://www.home-assistant.io/common-tasks/os/#backups) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown with diagnostics summaries, checklists, decision trees, change previews, and automation or dashboard plans] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only by default; write, reload, restart, update, restore, and security-sensitive actions require explicit scoped approval.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
