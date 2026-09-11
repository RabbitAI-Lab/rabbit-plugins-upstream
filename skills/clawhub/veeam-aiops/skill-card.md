## Description:

Veeam AIops helps agents operate Veeam Backup & Replication through governed CLI and MCP tools for health checks, diagnostics, backup jobs, restores, repositories, backups, infrastructure, sessions, and undo workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Developers, backup operators, and infrastructure teams use this skill to inspect Veeam Backup & Replication environments, triage failed jobs and repository capacity, run or stop backup jobs, list restore points, start VM restores, and follow asynchronous sessions. It is intended for Veeam Backup & Replication only and is out of scope for other backup products, hypervisor lifecycle operations, Kubernetes, or cloud providers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact Veeam write and restore actions.

Mitigation: Use a dedicated least-privilege Veeam account, start with read-only or restricted permissions, and require human review before stop, disable, undo, or restore actions.

Risk: Restore and session stop workflows can be irreversible or have no undo token.

Mitigation: Use dry-run previews where available, verify the resolved restore target, and confirm destructive actions outside the model before execution.

Risk: Credential handling includes a legacy plaintext password fallback and a master password for non-interactive use.

Mitigation: Use the encrypted secrets store, avoid plaintext .env password fallback, and do not hardcode the master password in shared MCP configuration.

Risk: The scanner reports weak built-in approval controls.

Mitigation: Rely on Veeam account permissions and external human approval policy for authorization, treating the skill's audit and risk labels as visibility rather than permission gates.

## Reference(s):

- [Veeam AIops project homepage](https://github.com/AIops-tools/Veeam-AIops)
- [Veeam AIops ClawHub release](https://clawhub.ai/zw008/skills/veeam-aiops)
- [Capabilities](references/capabilities.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [CLI Reference](references/cli-reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and text with inline shell commands, configuration snippets, and structured MCP tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return operational findings, audit-oriented status, dry-run previews, undo identifiers for reversible writes, and session progress details.]

## Skill Version(s):

0.12.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
