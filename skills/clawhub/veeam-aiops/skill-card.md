## Description:

Operates Veeam Backup & Replication through audited CLI and MCP workflows for health checks, diagnostics, backup jobs, restore points, repositories, backups, infrastructure inventory, and sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Backup operators, SREs, and IT administrators use this skill to inspect Veeam Backup & Replication health, diagnose backup failures and repository capacity issues, run or stop jobs, list restore points, and initiate governed restore workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact Veeam actions can stop sessions, disable jobs, start restores, or apply undo without a built-in read-only mode or mandatory approval gate.

Mitigation: Use a dedicated least-privilege Veeam account, prefer read-only or restricted roles for agent sessions, and require an external approval process before restore, stop, disable, or undo actions.

Risk: Credentials and the master password grant access to Veeam operations.

Mitigation: Use the encrypted credential store, avoid plaintext .env secrets, protect VEEAM_AIOPS_MASTER_PASSWORD, and rotate credentials according to local policy.

Risk: Restore and stop workflows can affect running backups or production virtual machines.

Mitigation: Use dry-run previews where available, confirm restore-point and job identifiers against current tool output, and review the local audit trail after governed operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/veeam-aiops)
- [Project homepage from ClawHub metadata](https://github.com/AIops-tools/Veeam-AIops)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands and structured MCP-oriented task guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to invoke Veeam CLI or MCP tools; read outputs can include JSON-like envelopes for paginated or truncated results.]

## Skill Version(s):

0.15.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
