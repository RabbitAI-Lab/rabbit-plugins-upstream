## Description:

Veeam AIops helps agents operate Veeam Backup & Replication through governed CLI and MCP workflows for health checks, diagnostics, job control, repository and backup inventory, restore point listing, VM restore starts, and session progress.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Backup administrators, SREs, and operations engineers use this skill to inspect and operate Veeam Backup & Replication environments from an agent. It supports read-only health and RCA workflows as well as governed job, restore, session, and undo operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes high-impact write and restore actions without an enforced read-only or approval gate for agent or MCP use.

Mitigation: Use a dedicated least-privilege Veeam account, preferably read-only for diagnostics, and expose write tools only when the operator accepts the risks of job stops, schedule changes, session cancellation, and irreversible VM restore actions.

Risk: The master password can be placed in MCP client configuration for non-interactive use, and legacy plaintext .env secrets are still honored as a fallback.

Mitigation: Avoid plaintext master-password storage where possible, migrate legacy .env secrets into the encrypted store, and restrict access to local configuration files.

Risk: Restore and session cancellation workflows can affect live backup operations, and VM restore actions may be irreversible.

Mitigation: Use dry-run previews, confirm the resolved target before restore actions, and validate write operations in the intended Veeam environment before relying on autonomous execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/veeam-aiops)
- [Project homepage](https://github.com/AIops-tools/Veeam-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-style MCP or tool outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some list, session, restore point, and ranking outputs include truncation, scope, or ordering indicators that the agent should preserve when reporting results.]

## Skill Version(s):

0.16.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
